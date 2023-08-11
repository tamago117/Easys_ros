from controller.PID import PID

class PID_controller:
    def __init__(self, config):
        # PIDパラメータ
        self.rollP = config["rollP"]
        self.rollI = config["rollI"]
        self.rollD = config["rollD"]
        self.pitchP = config["pitchP"]
        self.pitchI = config["pitchI"]
        self.pitchD = config["pitchD"]
        self.dt = config["dt"]

        self.roll_PID = PID(self.rollP, self.rollI, self.rollD, self.dt, -999, 999)
        self.pitch_PID = PID(self.pitchP, self.pitchI, self.pitchD, self.dt, -999, 999)

        # 偏差の保存
        self.pre_roll_error = 0
        self.roll_integral = 0
        self.pre_pitch_error = 0
        self.pitch_integral = 0

        # PIDの出力
        self.roll_PID_output = 0
        self.pitch_PID_output = 0

    def control(self, current_roll, current_pitch, Vx, Vz, yaw_rate):#軸のトルクを各スラスターへの力に変換します
        # カメラの視線の方向をX軸，重力方向をZ軸，ロボット後方からみて右側をY軸とする．座標原点は９軸座標の原点
        # Vx: Z方向の速度 (+-0の3値でいいかもしれない)
        # Vz :　Z方向の速度
        # yow_rate: Yaw方向の角速度

        
        # スラスターの出力 ロボット後方からみて左から0から3
        # 1.0となっているものは適当に調整するパラメータです．実験してみてから調整してみてください
        # これらのパラメータは長さの次元を持っています．トルクへの変換だと思ってもらえればいいと思います．
        kr = 1.0
        kp = 1.0
        ky = 1.0

        T1 = 0.5*(kp*self.pitch_PID.control(current_pitch, 0) + kr*self.roll_PID.control(current_roll, 0)) + Vz
        T2 = 0.5*(kp*self.pitch_PID.control(current_pitch, 0) - kr*self.roll_PID.control(current_roll, 0)) + Vz
        T0 = Vx - yaw_rate*ky
        T3 = Vx + yaw_rate*ky
        
        # 1つめの要素：前進(x方向) & YOWへの作用 　左下
        # 2つめの要素：YOWへの作用 & rollへの作用　& Picthへの作用　左上
        # 3つめの要素：YOWへの作用 & rollへの作用　& Picthへの作用　右上
        # 4つめの要素：前進(x方向) & YOWへの作用 　右下
        thruster = [T0,T1,T2,T3]
        return thruster