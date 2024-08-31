# Script1

import maya.cmds as cmds

# Define source and target bones

source_bones = ['hand_r', 'hand_r']

target_bones = ['ik_hand_gun', 'ik_hand_r']

for i in range(len(target_bones)):

    # Get the start and end frames of the animation
    start_frame = cmds.playbackOptions(query=True, minTime=True)
    end_frame = cmds.playbackOptions(query=True, maxTime=True)

    # Iterate through each frame
    for frame in range(int(start_frame), int(end_frame) + 1):
        # Set the current time to the frame
        cmds.currentTime(frame)

        # Get the transform values from the source bone
        transforms = cmds.xform(source_bones[i], query=True, worldSpace=True, matrix=True)

        # Apply the transform values to the target bone
        cmds.xform(target_bones[i], worldSpace=True, matrix=transforms)

        # Key the target bone to ensure the transformation is recorded
        cmds.setKeyframe(target_bones[i])

# Script2

import maya.cmds as cmds

# Get the start and end frames of the timeline
start_frame = cmds.playbackOptions(q=True, min=True)
end_frame = cmds.playbackOptions(q=True, max=True)

# Loop through all frames
for frame in range(int(start_frame), int(end_frame) + 1):
    cmds.currentTime(frame)
    
    # Get the position of the ik_hand_l joint
    ik_hand_pos = cmds.xform('ik_hand_l', q=True, ws=True, t=True)
    
    # Set the position of the Character2_Ctrl_LeftWristEffector to the ik_hand_l position
    cmds.xform('Character1_Ctrl_LeftWristEffector', ws=True, t=ik_hand_pos)

    cmds.setKeyframe('Character1_Ctrl_LeftWristEffector')



#Script3


import maya.cmds as cmds

# Define source and target bones

source_bones = ['hand_l']

target_bones = ['ik_hand_l']

for i in range(len(target_bones)):

    # Get the start and end frames of the animation
    start_frame = cmds.playbackOptions(query=True, minTime=True)
    end_frame = cmds.playbackOptions(query=True, maxTime=True)

    # Iterate through each frame
    for frame in range(int(start_frame), int(end_frame) + 1):
        # Set the current time to the frame
        cmds.currentTime(frame)

        # Get the transform values from the source bone
        transforms = cmds.xform(source_bones[i], query=True, worldSpace=True, matrix=True)

        # Apply the transform values to the target bone
        cmds.xform(target_bones[i], worldSpace=True, matrix=transforms)

        # Key the target bone to ensure the transformation is recorded
        cmds.setKeyframe(target_bones[i])
