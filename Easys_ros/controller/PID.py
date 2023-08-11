# pid class

class PID:
    def __init__(self, kp, ki, kd, dt, min_output_val, max_output_val):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.dt = dt
        self.min = min_output_val
        self.max = max_output_val
        self.integral = 0
        self.previous_error = 0

    def control(self, control_value, setpoint):
        error = control_value - setpoint
        self.integral += error * self.dt
        derivative = (error - self.previous_error) / self.dt
        output = self.kp * error + self.ki * self.integral + self.kd * derivative
        self.previous_error = error
        
        if output > self.max:
            output = self.max
        elif output < self.min:
            output = self.min
        return output

    def reset(self):
        self.integral = 0
        self.previous_error = 0