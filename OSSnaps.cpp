

#include <iostream>
#include <thread>
#include <ctime>
#include <ctype.h>
#include <cuda_runtime.h>
//#include <libcpuid.h>
#include <vector>

using namespace std;

int main(){

    size_t free;
    size_t total;
    cudaMemGetInfo(&free, &total);

    cudaDeviceProp currentDevice;
    int present = thread::hardware_concurrency();

    cout<<"Available Memory: "<<free<<" bytes, Total Memory: "<<total<<" bytes"<< endl;
    cout<<"Threads Available: "<<present<<endl;


    return 0;
}


class SystemInfoAggregator
{
    private:
        static size_t class_free;
        static size_t class_total;
        static int class_DeviceCount;
        static int class_cpuCount;
        static int class_gpuCount;
        static time_t startTime;
        time_t now;
        struct dataAggregator
        {
            time_t timestamp;
            size_t free = NULL;
            size_t total = class_free;
            int DeviceCount = class_DeviceCount;
            int cpuCount = class_cpuCount;
            int gpuCount = class_gpuCount;
            cudaDeviceProp *deviceCache;
        };


        dataAggregator *localCopy;
        vector<dataAggregator> dataPile;

        void newDataPoint()
        {

            dataPile.push_back(getCurrentInfo())
        }

        dataAggregator getCurrentInfo()
        {
            localCopy = new dataAggregator;
            time(&now)
            localCopy.timeStamp = difftime(startTime, now)
            cudaMemGetInfo(&localCopy.free, &localCopy.total)
            getDeviceData(localCopy);
        }
        


        void getDeviceData(dataAggregator *localCopy)
        {
            if (localCopy.gpuCount!=NULL){
                cudaDeviceProp *localCache = new cudaDeviceProp[localCopy.gpuCount];
                for(int i=0; i<localCopy.gpuCount; i++)
                {
                    cudaGetDeviceProperties(&localCopy.deviceCache[i], i);
                }
            }

        }


    public:
        SystemInfoAggregator()
        {
            time(&startTime);
            cudaGetDeviceCount(&localCopy.gpuCount); //load original number of devices
            cudaMemGetInfo(&localCopy.free, &localCopy.total); //Using this to just get the total mem available and an initial snapshot
            localCopy.cpuCount = thread::hardware_concurrency(); //Getting threadCount
            localCopy.deviceCache = new cudaDeviceProp[localCopy.gpuCount];
        }   
        ~SystemInfoAggregator()
        {
            
        }

        
};