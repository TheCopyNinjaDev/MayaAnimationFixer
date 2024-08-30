import maya.cmds as cmds

# Replace with the name of the joint you want to unkey
source_bone = 'ik_hand_l'

# Remove all keyframes from the joint
cmds.cutKey(source_bone, clear=True)

# Define source and target bones

target_bone = 'hand_l'

for i in range(len(target_bone)):

    # Get the start and end frames of the animation
    start_frame = cmds.playbackOptions(query=True, minTime=True)
    end_frame = cmds.playbackOptions(query=True, maxTime=True)

    # Iterate through each frame
    for frame in range(int(start_frame), int(end_frame) + 1):
        # Set the current time to the frame
        cmds.currentTime(frame)

        # Get the transform values from the source bone
        transforms = cmds.xform(source_bone, query=True, worldSpace=True, matrix=True)

        # Apply the transform values to the target bone
        cmds.xform(target_bone, worldSpace=True, matrix=transforms)

        # Key the target bone to ensure the transformation is recorded
        cmds.setKeyframe(target_bone)