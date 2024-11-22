# ORB-SLAM3 Keyframe Trajectory Viewer

This guide provides instructions to update the `myvideo.cpp` file, add the Python script for trajectory visualization, and rebuild the ORB-SLAM3 project.

---

## Instructions

### Step 1: Add the Python Visualization Script
1. Copy the provided Python script to the following location:
   ```
   ORB_SLAM3/Examples/Monocular/plot_and_save_keyframes.py
   ```
2. Make sure the Python script is configured to read the generated trajectory file:
   ```python
   trajectory_file = "MyVideoKeyFrameTrajectoryTUMFormat.txt"
   ```

---

### Step 2: Update `myvideo.cpp`
1. Open the `myvideo.cpp` file located in:
   ```
   ORB_SLAM3/Examples/Monocular/myvideo.cpp
   ```
2. Add the following lines **before shutting down the SLAM system** to save the trajectory:
   ```cpp
   SLAM.SaveKeyFrameTrajectoryTUM("MyVideoKeyFrameTrajectoryTUMFormat.txt");
   system("python3 /home/ben/Dev/ORB_SLAM3/Examples/Monocular/plot_and_save_keyframes.py"); // make sure to change the user to your own
   ```
   This will save the keyframe trajectory data into a file named `MyVideoKeyFrameTrajectoryTUMFormat.txt` in the current working directory.

3. Save the changes to `myvideo.cpp`.

---

### Step 3: Rebuild ORB-SLAM3
1. Rebuild the ORB-SLAM3 project to include the updated `myvideo.cpp`:
   ```bash
   cd ~/Dev/ORB_SLAM3/
   ./build.sh
   ```

---

### Step 4: Run the SLAM System and Generate the Trajectory
1. Run your updated `myvideo` example to execute ORB-SLAM3 and generate the trajectory file:
   ```bash
   cd ~/Dev/ORB_SLAM3/Examples/Monocular
   ./myvideo
   ```
2. Verify that the `KeyFrameTrajectoryTUMFormat.txt` file is created in the same directory.

---

### If you just want to view the Keyframe data already generated by ORBSLAM 3
1. Navigate to the `Examples/Monocular` directory:
   ```bash
   cd ORB_SLAM3/Examples/Monocular
   ```
2. Run the Python script to visualize the trajectory:
   ```bash
   python3 plot_and_save_keyframes.py
   ```

---

