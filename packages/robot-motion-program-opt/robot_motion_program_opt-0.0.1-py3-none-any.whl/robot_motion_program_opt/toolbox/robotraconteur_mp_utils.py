from contextlib import suppress
import numpy as np
from general_robotics_toolbox import *
from pandas import read_csv
import sys
from .robots_def import *
from .error_check import *
from .toolbox_circular_fit import *
from .lambda_calc import *
from .dual_arm import *
import RobotRaconteur as RR
from RobotRaconteurCompanion.Util.GeometryUtil import GeometryUtil

class MotionSendRobotRaconteurMP(object):
    def __init__(self, robot_mp=None, node=None):
        self._robot_mp = robot_mp
        if robot_mp is not None and node is None:
            self._node = robot_mp.RRGetNode()
        else:
            self._node = node

        self._robot_const = self._node.GetConstants("com.robotraconteur.robotics.robot", self._robot_mp)
        self._abb_robot_const = self._node.GetConstants("experimental.abb_robot", self._robot_mp)
        self._abb_robot_mp_const = self._node.GetConstants("experimental.abb_robot.motion_program", self._robot_mp)

        self._halt_mode = self._robot_const["RobotCommandMode"]["halt"]
        self._motion_program_mode = self._abb_robot_const["ABBRobotCommandMode"]["motion_program"]
        self._cir_path_mode_switch = self._abb_robot_mp_const["CirPathModeSwitch"]

        self._robot_pose_type = self._node.GetStructureType("experimental.robotics.motion_program.RobotPose",self._robot_mp)
        self._moveabsj_type = self._node.GetStructureType("experimental.robotics.motion_program.MoveAbsJCommand",self._robot_mp)
        self._movej_type =  self._node.GetStructureType("experimental.robotics.motion_program.MoveJCommand",self._robot_mp)
        self._movel_type = self._node.GetStructureType("experimental.robotics.motion_program.MoveLCommand",self._robot_mp)
        self._movec_type = self._node.GetStructureType("experimental.robotics.motion_program.MoveCCommand",self._robot_mp)
        self._settool_type = self._node.GetStructureType("experimental.robotics.motion_program.SetToolCommand",self._robot_mp)
        self._setpayload_type = self._node.GetStructureType("experimental.robotics.motion_program.SetPayloadCommand",self._robot_mp)
        self._waittime_type = self._node.GetStructureType("experimental.robotics.motion_program.WaitTimeCommand",self._robot_mp)
        self._cirpathmode_type = self._node.GetStructureType("experimental.abb_robot.motion_program.CirPathModeCommand",self._robot_mp)
        self._motionprogram_type = self._node.GetStructureType("experimental.robotics.motion_program.MotionProgram",self._robot_mp)
        self._toolinfo_type = self._node.GetStructureType("com.robotraconteur.robotics.tool.ToolInfo",self._robot_mp)
        self._payloadinfo_type = self._node.GetStructureType("com.robotraconteur.robotics.payload.PayloadInfo",self._robot_mp)
        self._transform_dt = self._node.GetNamedArrayDType("com.robotraconteur.geometry.Transform",self._robot_mp)
        self._spatialinertia_dt = self._node.GetNamedArrayDType("com.robotraconteur.geometry.SpatialInertia",self._robot_mp)

        self._geom_util = GeometryUtil(self._node, self._robot_mp)

    def robot_pose(self,p,q,joint_seed):
        ret = self._robot_pose_type()
        ret.tcp_pose[0]["orientation"]["w"] = q[0]
        ret.tcp_pose[0]["orientation"]["x"] = q[1]
        ret.tcp_pose[0]["orientation"]["y"] = q[2]
        ret.tcp_pose[0]["orientation"]["z"] = q[3]
        ret.tcp_pose[0]["position"]["x"] = p[0]*1e-3
        ret.tcp_pose[0]["position"]["y"] = p[1]*1e-3
        ret.tcp_pose[0]["position"]["z"] = p[2]*1e-3

        ret.joint_position_seed=joint_seed

        return ret

    def moveabsj(self,j,velocity,blend_radius,fine_point=False):
        cmd = self._moveabsj_type()
        cmd.joint_position = j
        cmd.tcp_velocity = velocity
        cmd.blend_radius = blend_radius
        cmd.fine_point = fine_point
        return RR.VarValue(cmd,"experimental.robotics.motion_program.MoveAbsJCommand")

    def movel(self,robot_pose,velocity,blend_radius,fine_point=False):
        cmd = self._movel_type()
        cmd.tcp_pose = robot_pose
        cmd.tcp_velocity = velocity*1e-3
        cmd.blend_radius = blend_radius*1e-1
        cmd.fine_point = fine_point
        return RR.VarValue(cmd,"experimental.robotics.motion_program.MoveLCommand")

    def movej(self,robot_pose,velocity,blend_radius,fine_point=False):
        cmd = self._movej_type()
        cmd.tcp_pose = robot_pose
        cmd.tcp_velocity = velocity*1e-3
        cmd.blend_radius = blend_radius*1e-3
        cmd.fine_point = fine_point
        return RR.VarValue(cmd,"experimental.robotics.motion_program.MoveJCommand")

    def movec(self,robot_via_pose,robot_pose,velocity,blend_radius,fine_point=False):
        cmd = self._movec_type()
        cmd.tcp_pose = robot_pose
        cmd.tcp_via_pose = robot_via_pose
        cmd.tcp_velocity = velocity*1e-3
        cmd.blend_radius = blend_radius*1e-3
        cmd.fine_point = fine_point
        return RR.VarValue(cmd,"experimental.robotics.motion_program.MoveCCommand")
    
    def moveL_target(self,robot,q,point):
        quat=R2q(robot.fwd(q).R)
        robt = self.robot_pose([point[0], point[1], point[2]], [ quat[0], quat[1], quat[2], quat[3]], q)
        return robt

    def moveC_target(self,robot,q1,q2,point1,point2):
        quat1=R2q(robot.fwd(q1).R)
        cf1=quadrant(q1,robot)
        quat2=R2q(robot.fwd(q2).R)
        cf2=quadrant(q2,robot)
        robt1 = self.robot_pose([point1[0], point1[1], point1[2]], [ quat1[0], quat1[1], quat1[2], quat1[3]], q1)
        robt2 = self.robot_pose([point2[0], point2[1], point2[2]], [ quat2[0], quat2[1], quat2[2], quat2[3]], q2)
        return robt1, robt2

    def moveJ_target(self,q):
        
        return q

    def waittime(self, t):
        wt = self._waittime_type()
        wt.time = t
        return (RR.VarValue(wt,"experimental.robotics.motion_program.WaitTimeCommand"))

    def settool(self, robot):
        toolinfo = self._toolinfo_type()
        toolinfo.tcp = self._geom_util.rox_transform_to_transform(rox.Transform(robot.R_tool, np.multiply(robot.p_tool,1e-3)))

        ii = np.zeros((1,),dtype=self._spatialinertia_dt)
        ii[0]["m"] = 1e-3
        ii[0]["com"] = (0,0,1e-3)
        ii[0]["ixx"] = 1e-3
        ii[0]["ixy"] = 0
        ii[0]["ixz"] = 0
        ii[0]["iyy"] = 1e-3
        ii[0]["iyz"] = 0
        ii[0]["izz"] = 1e-3
        toolinfo.inertia = ii
        #toolinfo.inertia = RRN.ArrayToNamedArray([0.1,0,0,0.01,.001,0,0,.001,0,.001],)

        settool = self._settool_type()
        settool.tool_info = toolinfo
        return RR.VarValue(settool,"experimental.robotics.motion_program.SetToolCommand")

    def convert_motion_program(self,robot,primitives,breakpoints,p_bp,q_bp,speed,zone):
        
        #mp = MotionProgram(tool=tooldata(True,pose(robot.p_tool,R2q(robot.R_tool)),loaddata(1,[0,0,0.001],[1,0,0,0],0,0,0)))

        setup_cmds=[self.settool(robot)]

        ###change cirpath mode
        mp_cmds = []
        cirpath = self._cirpathmode_type()
        cirpath.switch = self._cir_path_mode_switch["ObjectFrame"]
        mp_cmds.append(RR.VarValue(cirpath,"experimental.abb_robot.motion_program.CirPathModeCommand"))


        for i in range(len(primitives)):
            if 'movel' in primitives[i]:

                robt = self.moveL_target(robot,q_bp[i][0],p_bp[i][0])
                if type(speed) is list:
                    if type(zone) is list:
                        mp_cmds.append(self.movel(robt,speed[i],zone[i]))
                    else:
                        mp_cmds.append(self.movel(robt,speed[i],zone))
                else:
                    if type(zone) is list:
                        mp_cmds.append(self.movel(robt,speed,zone[i]))
                    else:
                        mp_cmds.append(self.movel(robt,speed,zone))
                

            elif 'movec' in primitives[i]:
                robt1, robt2 = self.moveC_target(robot,q_bp[i][0],q_bp[i][1],p_bp[i][0],p_bp[i][1])
                if type(speed) is list:
                    if type(zone) is list:
                        mp_cmds.append(self.movec(robt1,robt2,speed[i],zone[i]))
                    else:
                        mp_cmds.append(self.movec(robt1,robt2,speed[i],zone))
                else:
                    if type(zone) is list:
                        mp_cmds.append(self.movec(robt1,robt2,speed,zone[i]))
                    else:
                        mp_cmds.append(self.movec(robt1,robt2,speed,zone))

            elif 'movej' in primitives[i]:
                robt = self.moveL_target(robot,q_bp[i][0],p_bp[i][0])
                if type(speed) is list:
                    if type(zone) is list:
                        mp_cmds.append(self.movej(robt,speed[i],zone[i]))
                    else:
                        mp_cmds.append(self.movej(robt,speed[i],zone))
                else:
                    if type(zone) is list:
                        mp_cmds.append(self.movej(robt,speed,zone[i]))
                    else:
                        mp_cmds.append(self.movej(robt,speed,zone))

            else: # moveabsj
                jointt = self.moveJ_target(q_bp[i][0])
                if i==0:
                    mp_cmds.append(self.moveabsj(jointt,0.5,0.1,True))
                    mp_cmds.append(self.waittime(1))
                    mp_cmds.append(self.moveabsj(jointt,0.5,0.1,True))
                    mp_cmds.append(self.waittime(0.1))
                else:
                    if type(speed) is list:
                        if type(zone) is list:
                            mp_cmds.append(self.moveabsj(jointt,speed[i],zone[i]))
                        else:
                            mp_cmds.append(self.moveabsj(jointt,speed[i],zone))
                    else:
                        if type(zone) is list:
                            mp_cmds.append(self.moveabsj(jointt,speed,zone[i]))
                        else:
                            mp_cmds.append(self.moveabsj(jointt,speed,zone))
        ###add sleep at the end to wait for train_data transmission
        mp_cmds.append(self.waittime(0.1))

        mp = self._motionprogram_type()

        mp.motion_setup_commands = setup_cmds
        mp.motion_program_commands = mp_cmds

        return mp

    def exec_motions(self,robot,primitives,breakpoints,p_bp,q_bp,speed,zone):
        
        self._robot_mp.disable_motion_program_mode()
        self._robot_mp.enable_motion_program_mode()

        mp=self.convert_motion_program(robot,primitives,breakpoints,p_bp,q_bp,speed,zone)

        mp_gen = self._robot_mp.execute_motion_program_record(mp, False)
        res = None

        with suppress(RR.StopIterationException):
            while True:
                res = mp_gen.Next()

        recording_gen = self._robot_mp.read_recording(res.recording_handle)
        recording = recording_gen.NextAll()[0]

        self._robot_mp.clear_recordings()

        return recording

    def extend(self,robot,q_bp,primitives,breakpoints,p_bp,extension_start=100,extension_end=100):
        p_bp_extended=copy.deepcopy(p_bp)
        q_bp_extended=copy.deepcopy(q_bp)
        ###initial point extension
        pose_start=robot.fwd(q_bp[0][0])
        p_start=pose_start.p
        R_start=pose_start.R
        pose_end=robot.fwd(q_bp[1][-1])
        p_end=pose_end.p
        R_end=pose_end.R
        if 'movel' in primitives[1]:
            #find new start point
            slope_p=p_end-p_start
            slope_p=slope_p/np.linalg.norm(slope_p)
            p_start_new=p_start-extension_start*slope_p        ###extend 5cm backward

            #find new start orientation
            k,theta=R2rot(R_end@R_start.T)
            theta_new=-extension_start*theta/np.linalg.norm(p_end-p_start)
            R_start_new=rot(k,theta_new)@R_start

            #solve invkin for initial point
            p_bp_extended[0][0]=p_start_new
            q_bp_extended[0][0]=car2js(robot,q_bp[0][0],p_start_new,R_start_new)[0]

        elif 'movec' in primitives[1]:
            #define circle first
            pose_mid=robot.fwd(q_bp[1][0])
            p_mid=pose_mid.p
            R_mid=pose_mid.R

            center, radius=circle_from_3point(p_start,p_end,p_mid)

            #find desired rotation angle
            angle=extension_start/radius

            #find new start point
            plane_N=np.cross(p_end-center,p_start-center)
            plane_N=plane_N/np.linalg.norm(plane_N)
            R_temp=rot(plane_N,angle)
            p_start_new=center+R_temp@(p_start-center)

            #modify mid point to be in the middle of new start and old end (to avoid RS circle uncertain error)
            modified_bp=arc_from_3point(p_start_new,p_end,p_mid,N=3)
            p_bp_extended[1][0]=modified_bp[1]

            #find new start orientation
            k,theta=R2rot(R_end@R_start.T)
            theta_new=-extension_start*theta/np.linalg.norm(p_end-p_start)
            R_start_new=rot(k,theta_new)@R_start

            #solve invkin for initial point
            p_bp_extended[0][0]=p_start_new
            q_bp_extended[0][0]=car2js(robot,q_bp[0][0],p_start_new,R_start_new)[0]


        else:
            #find new start point
            J_start=robot.jacobian(q_bp[0][0])
            qdot=q_bp[0][0]-q_bp[1][0]
            v=np.linalg.norm(J_start[3:,:]@qdot)
            t=extension_start/v
            q_bp_extended[0][0]=q_bp[0][0]+qdot*t
            p_bp_extended[0][0]=robot.fwd(q_bp_extended[0][0]).p

        ###end point extension
        pose_start=robot.fwd(q_bp[-2][-1])
        p_start=pose_start.p
        R_start=pose_start.R
        pose_end=robot.fwd(q_bp[-1][-1])
        p_end=pose_end.p
        R_end=pose_end.R

        if 'movel' in primitives[-1]:
            #find new end point
            slope_p=(p_end-p_start)/np.linalg.norm(p_end-p_start)
            p_end_new=p_end+extension_end*slope_p        ###extend 5cm backward

            #find new end orientation
            k,theta=R2rot(R_end@R_start.T)
            slope_theta=theta/np.linalg.norm(p_end-p_start)
            R_end_new=rot(k,extension_end*slope_theta)@R_end

            #solve invkin for end point
            q_bp_extended[-1][0]=car2js(robot,q_bp[-1][0],p_end_new,R_end_new)[0]
            p_bp_extended[-1][0]=p_end_new


        elif  'movec' in primitives[-1]:
            #define circle first
            pose_mid=robot.fwd(q_bp[-1][0])
            p_mid=pose_mid.p
            R_mid=pose_mid.R
            center, radius=circle_from_3point(p_start,p_end,p_mid)

            #find desired rotation angle
            angle=extension_end/radius

            #find new end point
            plane_N=np.cross(p_start-center,p_end-center)
            plane_N=plane_N/np.linalg.norm(plane_N)
            R_temp=rot(plane_N,angle)
            p_end_new=center+R_temp@(p_end-center)

            #modify mid point to be in the middle of new end and old start (to avoid RS circle uncertain error)
            modified_bp=arc_from_3point(p_start,p_end_new,p_mid,N=3)
            p_bp_extended[-1][0]=modified_bp[1]

            #find new end orientation
            k,theta=R2rot(R_end@R_start.T)
            theta_new=extension_end*theta/np.linalg.norm(p_end-p_start)
            R_end_new=rot(k,theta_new)@R_end

            #solve invkin for end point
            q_bp_extended[-1][-1]=car2js(robot,q_bp[-1][-1],p_end_new,R_end_new)[0]
            p_bp_extended[-1][-1]=p_end_new   #midpoint not changed

        else:
            #find new end point
            J_end=robot.jacobian(q_bp[-1][0])
            qdot=q_bp[-1][0]-q_bp[-2][0]
            v=np.linalg.norm(J_end[3:,:]@qdot)
            t=extension_end/v
            
            q_bp_extended[-1][0]=q_bp[-1][-1]+qdot*t
            p_bp_extended[-1][0]=robot.fwd(q_bp_extended[-1][-1]).p

        return p_bp_extended,q_bp_extended

    def logged_data_analysis(self,robot,log_results,realrobot=True):
        cmd_num=log_results.command_number
        #find closest to 5 cmd_num
        idx = np.absolute(cmd_num-5).argmin()
        start_idx=np.where(cmd_num==cmd_num[idx])[0][0]
        curve_exe_js=log_results.joints[start_idx:]
        timestamp=log_results.time[start_idx:]
        ###filter noise
        timestamp, curve_exe_js=lfilter(timestamp, curve_exe_js)

        speed=[0]
        lam=[0]
        curve_exe=[]
        curve_exe_R=[]
        for i in range(len(curve_exe_js)):
            robot_pose=robot.fwd(curve_exe_js[i],qlim_override=True)
            curve_exe.append(robot_pose.p)
            curve_exe_R.append(robot_pose.R)
            if i>0:
                lam.append(lam[-1]+np.linalg.norm(curve_exe[i]-curve_exe[i-1]))
            try:
                if timestamp[i-1]!=timestamp[i] and np.linalg.norm(curve_exe_js[i-1]-curve_exe_js[i])!=0:
                    speed.append(np.linalg.norm(curve_exe[-1]-curve_exe[-2])/(timestamp[i]-timestamp[i-1]))
                else:
                    speed.append(speed[-1])      
            except IndexError:
                pass

        speed=moving_average(speed,padding=True)
        return np.array(lam), np.array(curve_exe), np.array(curve_exe_R),np.array(curve_exe_js), np.array(speed), timestamp-timestamp[0]

    def chop_extension(self,curve_exe, curve_exe_R,curve_exe_js, speed, timestamp,p_start,p_end):
        start_idx=np.argmin(np.linalg.norm(p_start-curve_exe,axis=1))
        end_idx=np.argmin(np.linalg.norm(p_end-curve_exe,axis=1))

        #make sure extension doesn't introduce error
        if np.linalg.norm(curve_exe[start_idx]-p_start)>0.5:
            start_idx+=1
        if np.linalg.norm(curve_exe[end_idx]-p_end)>0.5:
            end_idx-=1

        curve_exe=curve_exe[start_idx:end_idx+1]
        curve_exe_js=curve_exe_js[start_idx:end_idx+1]
        curve_exe_R=curve_exe_R[start_idx:end_idx+1]
        speed=speed[start_idx:end_idx+1]
        lam=calc_lam_cs(curve_exe)

        return lam, curve_exe, curve_exe_R,curve_exe_js, speed, timestamp[start_idx:end_idx+1]-timestamp[start_idx]