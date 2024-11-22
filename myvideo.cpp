#include <opencv2/opencv.hpp>
#include "System.h"
#include <string>
#include <chrono>   // for time stamp
#include <iostream>
#include <cstdlib>

using namespace std;

//need to change to your own path
string parameterFile = "/home/ben/Dev/ORB_SLAM3/Examples/Monocular/myvideo.yaml";
string vocFile = "/home/ben/Dev/ORB_SLAM3/Vocabulary/ORBvoc.txt";
string videoFile = "/home/ben/Dev/ORB_SLAM3/Examples/Monocular/video.mp4";

int main(int argc, char **argv) {

    
    ORB_SLAM3::System SLAM(vocFile, parameterFile, ORB_SLAM3::System::MONOCULAR, true);

    
    cv::VideoCapture cap(videoFile);    // change to 1 if you want to use USB camera.
    
    auto start = chrono::system_clock::now();

    while (1) {
        cv::Mat frame;
        cap >> frame;   
        if ( frame.data == nullptr )
            break;

        // rescale because image is too large
        cv::Mat frame_resized;
        cv::resize(frame, frame_resized, cv::Size(640,480));

        auto now = chrono::system_clock::now();
        auto timestamp = chrono::duration_cast<chrono::milliseconds>(now - start);
        SLAM.TrackMonocular(frame_resized, double(timestamp.count())/1000.0);
        cv::waitKey(30);
    }
	
// Save the keyframe trajectory in TUM format
    SLAM.SaveKeyFrameTrajectoryTUM("MyVideoKeyFrameTrajectoryTUMFormat.txt");

// Optional: Save the full trajectory (all frames) in TUM format. Does not work in Monocular.
//  SLAM.SaveTrajectoryTUM("MyVideoFrameTrajectoryTUMFormat.txt");

    system("python3 /home/ben/Dev/ORB_SLAM3/Examples/Monocular/plot_and_save_keyframes.py");
    SLAM.Shutdown();

    return 0;
}