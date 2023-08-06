from rria_api.ned.connect_ned import ConnectNed
from rria_api.ned.action_ned import ActionNed
from rria_api.gen3.connect_gen3 import ConnectGen3
from rria_api.gen3.action_gen3 import ActionGen3
from time import sleep


class RobotAdapter:
    def __init__(self, preferences: list):
        self.ip_address = preferences[0]
        self.robot_type = preferences[1]

        # This atribute is used to store the general robot instance
        self.robot_instance = None

        # This atribute is used to store the general connection instance
        self.connection_instance = None

    def connect_robot(self):
        if self.robot_type == 'gen3':
            try:
                self.connection_instance = ConnectGen3(self.ip_address, ["admin", "admin"])
                self.robot_instance = self.connection_instance.connect_robot()

                return True

            except(Exception, ):
                print('The connection attempt failed. Check the physical connection to the robot and try again later.')

                return False

        if self.robot_type == 'ned':
            try:
                self.connection_instance = ConnectNed()
                self.robot_instance = self.connection_instance.connect_robot(self.ip_address)

                return True

            except(Exception, ):
                print('The connection attempt failed. Check the physical connection to the robot and try again later.')

                return False

        if self.robot_type == 'denso':
            pass

        if self.robot_type == 'test':
            sleep(1)
            return True

    def disconnect_robot(self):
        if self.robot_type == 'gen3':
            self.connection_instance.disconnect_robot()

        if self.robot_type == 'ned':
            self.connection_instance.disconnect_robot()

        if self.robot_type == 'denso':
            pass

        if self.robot_type == 'test':
            sleep(1)
            return True

    def safe_disconnect(self):
        if self.robot_type == 'gen3':
            ActionGen3(self.robot_instance).move_to_zero()
            self.connection_instance.disconnect_robot()

        if self.robot_type == 'ned':
            ActionNed(self.robot_instance).move_to_home()
            self.connection_instance.disconnect_robot()

        if self.robot_type == 'denso':
            ...

        if self.robot_type == 'test':
            sleep(1)
            return True

    # Move Joints/Cartesian methods

    def move_joints(self, j1, j2, j3, j4, j5, j6):
        if self.robot_type == 'gen3':
            ActionGen3(self.robot_instance).move_joints([j1, j2, j3, j4, j5, j6])

        if self.robot_type == 'ned':
            ActionNed(self.robot_instance).move_joints(j1, j2, j3, j4, j5, j6)

        if self.robot_type == 'denso':
            ...

        if self.robot_type == 'test':
            sleep(1)
            return True

    def get_joints(self):
        if self.robot_type == 'gen3':
            return ActionGen3(self.robot_instance).get_joints()

        if self.robot_type == 'ned':
            return ActionNed(self.robot_instance).get_joints()

        if self.robot_type == 'denso':
            ...

        if self.robot_type == 'test':
            sleep(0.5)
            return ['J1', 'J2', 'J3', 'J4', 'J5', 'J6']

    def move_cartesian(self, x, y, z, roll, pitch, yaw):
        if self.robot_type == 'gen3':
            return ActionGen3(self.robot_instance).move_cartesian([x, y, z, roll, pitch, yaw])

        if self.robot_type == 'ned':
            return ActionNed(self.robot_instance).move_cartesian(x, y, z, roll, pitch, yaw)

        if self.robot_type == 'denso':
            ...

        if self.robot_type == 'test':
            sleep(1)
            return True

    def get_cartesian(self):
        if self.robot_type == 'gen3':
            return ActionGen3(self.robot_instance).get_cartesian()

        if self.robot_type == 'ned':
            return ActionNed(self.robot_instance).get_cartesian()

        if self.robot_type == 'denso':
            ...

        if self.robot_type == 'test':
            sleep(1)
            return True

    def move_to_home(self):
        if self.robot_type == 'gen3':
            ActionGen3(self.robot_instance).move_to_home()

        if self.robot_type == 'ned':
            ActionNed(self.robot_instance).move_to_home()

        if self.robot_type == 'denso':
            ...

        if self.robot_type == 'test':
            sleep(1)
            return True

    def move_to_zero(self):
        if self.robot_type == 'gen3':
            ActionGen3(self.robot_instance).move_to_zero()

        if self.robot_type == 'ned':
            ActionNed(self.robot_instance).move_to_zero()

        if self.robot_type == 'denso':
            ...

        if self.robot_type == 'test':
            sleep(1)
            return True

    def open_gripper(self):
        if self.robot_type == 'gen3':
            ActionGen3(self.robot_instance).open_gripper()

        if self.robot_type == 'ned':
            ActionNed(self.robot_instance).open_gripper()

        if self.robot_type == 'denso':
            ...

        if self.robot_type == 'test':
            sleep(1)
            return True

    def close_gripper(self):
        if self.robot_type == 'gen3':
            ActionGen3(self.robot_instance).close_gripper()

        if self.robot_type == 'ned':
            ActionNed(self.robot_instance).close_gripper()

        if self.robot_type == 'denso':
            ...

        if self.robot_type == 'test':
            sleep(1)
            return True

    # TODO: Ver a função de aumento de velocidade para o Gen3
    def set_velocity(self, velocity):
        if self.robot_type == 'gen3':
            ActionGen3(self.robot_instance).set_velocity(velocity)

        if self.robot_type == 'ned':
            ActionNed(self.robot_instance).set_velocity(velocity)

        if self.robot_type == 'denso':
            ...

        if self.robot_type == 'test':
            sleep(1)
            return True

    def calibrate(self):
        if self.robot_type == 'gen3':
            print('Gen3 NÃO necessita de calibração')

        if self.robot_type == 'ned':
            ActionNed(self.robot_instance).calibrate()

        if self.robot_type == 'denso':
            ...

        if self.robot_type == 'test':
            sleep(1)
            return True

    def go_to_sleep(self):
        if self.robot_type == 'gen3':
            ...

        if self.robot_type == 'ned':
            ActionNed(self.robot_instance).go_to_sleep()

        if self.robot_type == 'denso':
            ...

        if self.robot_type == 'test':
            sleep(1)
            return True
