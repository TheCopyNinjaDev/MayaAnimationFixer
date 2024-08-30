import maya.cmds as cmds

# Define source and target bones

source_bones = ['foot_l', 'foot_r', 'hand_r', 'hand_r', 'hand_l']

target_bones = ['ik_foot_l', 'ik_foot_r', 'ik_hand_gun', 'ik_hand_r', 'ik_hand_l']

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