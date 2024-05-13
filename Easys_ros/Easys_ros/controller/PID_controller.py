from .PID import PID

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

        # 初期のVxとVzの値
        self.prev_Vx = 0
        self.prev_Vz = 0
        self.prev_yaw_rate = 0
        # フィルタの定数
        self.alpha = 0.08  # 例えば0.2としてみましたが、実際には調整が必要です

    def control(self, current_roll, current_pitch, Vx, Vz, yaw_rate):#軸のトルクを各スラスターへの力に変換します
        # カメラの視線の方向をX軸，重力方向をZ軸，ロボット後方からみて右側をY軸とする．座標原点は９軸座標の原点
        # Vx: Z方向の速度 (+-0の3値でいいかもしれない)
        # Vz :　Z方向の速度
        # yow_rate: Yaw方向の角速度

        # ローパスフィルターでVxとVzを滑らかにする
        Vx_filtered = (1 - self.alpha) * self.prev_Vx + self.alpha * Vx
        Vz_filtered = (1 - self.alpha) * self.prev_Vz + self.alpha * Vz
        yaw_rate_filtered = (1 - self.alpha) * self.prev_yaw_rate + self.alpha * yaw_rate

        # 次のステップのために値を保存
        self.prev_Vx = Vx_filtered
        self.prev_Vz = Vz_filtered
        self.prev_yaw_rate = yaw_rate_filtered

        # スラスターの出力 ロボット後方からみて左から0から3
        # 1.0となっているものは適当に調整するパラメータです．実験してみてから調整してみてください
        # これらのパラメータは長さの次元を持っています．トルクへの変換だと思ってもらえればいいと思います．
        kr = 1.0
        kp = 1.0
        ky = 1.0
        T1 = -(0.5*(kp*self.pitch_PID.control(current_pitch, 0) + kr*self.roll_PID.control(current_roll, 0)) + Vz_filtered)
        T2 = -(0.5*(kp*self.pitch_PID.control(current_pitch, 0) - kr*self.roll_PID.control(current_roll, 0)) + Vz_filtered)
        T0 = Vx_filtered - yaw_rate_filtered*ky
        T3 = Vx_filtered + yaw_rate_filtered*ky

        # 1つめの要素：前進(x方向) & YOWへの作用 　左下
        # 2つめの要素：YOWへの作用 & rollへの作用　& Picthへの作用　左上
        # 3つめの要素：YOWへの作用 & rollへの作用　& Picthへの作用　右上
        # 4つめの要素：前進(x方向) & YOWへの作用 　右下
        thruster = [T0,T1,T2,T3]
        return thruster