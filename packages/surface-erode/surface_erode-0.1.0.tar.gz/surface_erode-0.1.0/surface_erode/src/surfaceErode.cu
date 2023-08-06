#include <cuda.h>
#include <cuda_runtime_api.h>
#include <dirent.h>
#include <iostream>
#include <stdio.h>
#include <string.h>
#include <sys/stat.h>

using namespace std;

#define CUDA_SAFE_CALL(x)                                                         \
{                                                                               \
	if (x != cudaSuccess)                                                         \
	{                                                                             \
		printf("  Cuda error %i occured in %s, line %i!\n", x, __FILE__, __LINE__); \
		printf("  Cuda error message:  %s\n", cudaGetErrorString(x));               \
		char buffer[256];                                                           \
		cin >> buffer;                                                              \
		exit(-1);                                                                   \
	}                                                                             \
}

typedef unsigned char uchar;

const int size_uchar = sizeof(uchar);

__device__ bool isBoundary(cudaSurfaceObject_t track_surf, int _x, int _y, int _z, int depth, int width, int height, bool interface)
{
	bool tag = false;
	uchar current_value;
	surf3Dread(&current_value, track_surf, _x, _y, _z, cudaBoundaryModeTrap);
	if (current_value <= 0)
		return tag;

	for (int k = _z - 1; k <= _z + 1; k++){
		for (int j = _y - 1; j <= _y + 1; j++){
			for (int i = _x - 1; i <= _x + 1; i++){
				if (((k > 0) && (k < depth)) && ((j > 0) && (j < height)) && ((i > 0) && (i < width))){
					if (i != _x || j != _y || k != _z) {
						unsigned char boundary_value;
						surf3Dread(&boundary_value, track_surf, i, j, k, cudaBoundaryModeTrap);
						// mask 交接面
						if (interface){
							if((boundary_value != current_value) && (boundary_value != 0)){
								tag = true;
								return tag;
							}
						}
						// mask 表面
						else {
							if (boundary_value != current_value) {
								tag = true;
								return tag;
							}
						}
					} // end if
				} // end if
			} // for i
		} // for j
	} // for k
	return tag;
}


__global__ void SurfaceErodePoint(cudaSurfaceObject_t track_surf, int *incluidos, int depth, int width, int height, bool interface)
{
	int x = blockIdx.x * blockDim.x + threadIdx.x;
	int y = blockIdx.y * blockDim.y + threadIdx.y;
	int z = blockIdx.z * blockDim.z + threadIdx.z;
	if ((x < width) && (y < height) && (z < depth))
	{
		bool boundary_tag = isBoundary(track_surf, x, y, z, depth, width, height, interface);
		__syncthreads();
		if (boundary_tag)
		{
			surf3Dwrite(uchar(0), track_surf, x * size_uchar, y, z, cudaBoundaryModeTrap);
			*incluidos += 1;
		}
	}
}


extern "C"
{
void SurfaceErodeEntrance(uchar *h_mask, int width, int height, int depth,  int erode_iterations, bool interface, int gpu)
{
	cudaSetDevice(gpu);
	size_t size_int = sizeof(int);

	// 开辟 GPU 内存: cuda_Array: track
	cudaChannelFormatDesc channelDesc = cudaCreateChannelDesc(8, 0, 0, 0, cudaChannelFormatKindUnsigned);
	cudaArray *d_mask;
	cudaExtent extent3D;
	extent3D.width = width;
	extent3D.depth = depth;
	extent3D.height = height;
	CUDA_SAFE_CALL(cudaMalloc3DArray((cudaArray **)&d_mask, &channelDesc, extent3D, cudaArraySurfaceLoadStore));

	int *h_incluidos = (int *)malloc(size_int);
	int *d_incluidos;
	CUDA_SAFE_CALL(cudaMalloc((void **)&d_incluidos, size_int));
	dim3 dimBlock(16, 16, 4);
	dim3 dimGrid(32, 32, (depth + 4) / 4);

	// 将 h_mask与 d_mask 绑定
	cudaMemcpy3DParms track_parms = {0};
	track_parms.srcPos = make_cudaPos(0, 0, 0);
	track_parms.dstPos = make_cudaPos(0, 0, 0);
	track_parms.srcPtr = make_cudaPitchedPtr(h_mask, width * size_uchar, width, height);
	track_parms.dstArray = d_mask;
	track_parms.extent = make_cudaExtent(width, height, depth);
	track_parms.kind = cudaMemcpyHostToDevice;
	CUDA_SAFE_CALL(cudaMemcpy3D(&track_parms));
	// 指定表面内存
	struct cudaResourceDesc resDesc;
	memset(&resDesc, 0, sizeof(resDesc));
	resDesc.resType = cudaResourceTypeArray;
	// 创建表面内存对象 并绑定 CUDA_Array
	resDesc.res.array.array = d_mask;
	cudaSurfaceObject_t mask_surf_obj = 0;
	cudaCreateSurfaceObject(&mask_surf_obj, &resDesc);

	int iterations = 1;
	do
	{
		*h_incluidos = 0;
		CUDA_SAFE_CALL(cudaMemcpy(d_incluidos, h_incluidos, size_int, cudaMemcpyHostToDevice));
		printf("iteration: %d\n", iterations);
		SurfaceErodePoint<<<dimGrid, dimBlock>>>(mask_surf_obj, d_incluidos, depth, width, height, interface);
		CUDA_SAFE_CALL(cudaDeviceSynchronize());
		CUDA_SAFE_CALL(cudaMemcpy(h_incluidos, d_incluidos, size_int, cudaMemcpyDeviceToHost));
		iterations++;
		if (iterations > erode_iterations)
		{
			break;
		}
	} while (*h_incluidos != 0);

	cudaMemcpy3DParms myParms = {0};
	myParms.srcArray = d_mask;
	myParms.srcPos = make_cudaPos(0, 0, 0);
	myParms.dstPos = make_cudaPos(0, 0, 0);
	myParms.dstPtr = make_cudaPitchedPtr(h_mask, width * size_uchar, width, height);
	myParms.extent = make_cudaExtent(width, height, depth);
	myParms.kind = cudaMemcpyDeviceToHost;
	CUDA_SAFE_CALL(cudaMemcpy3D(&myParms));

	free(h_incluidos);
	// 解除绑定并释放内存
	cudaFreeArray(d_mask);
	cudaDestroySurfaceObject(mask_surf_obj);
	cudaFree(d_incluidos);

}   // SurfaceErodeEntrance
}   // extern "C"
