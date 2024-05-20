# Assembly Instructions

## Contents
- 1. Preparation of Parts
- 2. Creation of Circuit Components
- 3. Assembly
- 4. Buoyancy Adjustment
- 5. Software Preparation

## 1. Preparation of Parts
### 1.1 Purchasing Parts
Purchase all the parts listed in the parts list below (excluding 3D printed parts).

- [Parts List](https://docs.google.com/spreadsheets/d/1spEkeJp3uywtmMTm2RyMCUT-x4rrJNMb/edit?usp=sharing&ouid=116393592539270427202&rtpof=true&sd=true)


![image](https://github.com/Honazo/Easys_ros/assets/63952012/cd761d00-b05f-438c-a78a-9fa95a636082)


### 1.2 Creating 3D Printed Parts

Print the parts from the 3D printer parts list below.

- [3D Printer Parts List](https://docs.google.com/spreadsheets/d/1m-tpGwKx88t4YWLlDcRS2Wr9CotMB-zd/edit?usp=sharing&ouid=116393592539270427202&rtpof=true&sd=true)

![image](https://github.com/Honazo/Easys_ros/assets/63952012/3e336ccb-949d-4b08-8d8e-af62c2321635)


Assuming a home-sized FDM 3D printer.

![3D Printer](https://github.com/Honazo/Easys_ros/assets/63952012/aeec14bd-fc2d-4e3f-a4ac-ccc087aac8fa)

Use ABS filament for 3D printing.

The front and rear flanges require waterproof printing. Set the infill structure density to 100% and print as finely as possible for layer spans.

## 2. Creation of Circuit Components

### 2.1 Main Circuit

The circuit diagram is as follows.

![Circuit Diagram](https://github.com/Honazo/Easys_ros/assets/63952012/6487e8e7-12b2-42f7-9a1a-7bbf0cc4ab7e)

Here is how it looks when assembled.

![Assembled Circuit](https://github.com/Honazo/Easys_ros/assets/63952012/ab8e0a15-5a58-4cfb-ac4f-dfc6b16a2c55)

Below is a CAD representation of the same circuit component.

![CAD Circuit](https://github.com/Honazo/Easys_ros/assets/63952012/4d56b683-03c3-4a9a-9a16-1bd4bd69a64c)

### 2.2 Connecting Connectors

#### 2.2.1 Cable Glands

Pre-thread the cables exiting the pressure vessel through cable glands.

Install three-hole cable glands for each of the three cables of the four thrusters and one-hole cable glands for the two-core power lines.

After threading the cable glands, fix them to the holes in the rear flange.

![Cable Glands](https://github.com/Honazo/Easys_ros/assets/63952012/44abfc17-d6d4-414a-ac50-613bca0fdfa9)

![More Cable Glands](https://github.com/Honazo/Easys_ros/assets/63952012/ae6b3736-ca55-459b-b670-bcd48589ace9)

For the LAN cable, cut it a few cm from the connector since it won’t fit through the cable gland. Thread the gland, secure it in the hole of the rear flange, then solder the cut ends back together.

![LAN Cable Modification](https://github.com/Honazo/Easys_ros/assets/63952012/f7571093-308c-4508-bb1f-da3c620806fe)

#### 2.2.2 Connecting the Connectors

After securing the cable glands, connect a T-connector to the power lines and a three-phase connector to the lines of the thrusters.

![T-Connector](https://github.com/Honazo/Easys_ros/assets/63952012/c88c3423-1f0d-49d4-a997-446f27048139)

Below is the first block of the circuit mount.

![Circuit Mount](https://github.com/Honazo/Easys_ros/assets/63952012/2862b783-b833-4fb0-b345-362af9da5a11)

Mount the parallel wired female T-connectors and the four vertically stacked ESCs side by side on the mount.

![ESC Mounting](https://github.com/Honazo/Easys_ros/assets/63952012/ff4dc029-8022-4a6c-97c0-8cf0c20adea6)

For each of the four ESCs, connect the power lines to the T-connectors and the three-phase output to the three-phase connectors.

#### 2.2.3 Step-Down Converter Circuit & Servo Controller

Run wires from the step-down converter as shown below.

![Step-Down Converter Wiring](https://github.com/Honazo/Easys_ros/assets/63952012/58ef4fdb-c10f-4b40-b6d4-5685c856a0a8)

Connect a T-connector to both the input and output voltage sides of the step-down converter.

Connect the ESC's signal input lines (black, red, white, yellow) to the servo controller's output terminals.

Connect ESC's ① black (GND), ② red (V+), ③ white (PWM) to the servo controller's ① black (GND), ② red (V+), ③ yellow (PWM). (Do not use the yellow line of the ESC.)

![Servo Controller Connections](https://github.com/Honazo/Easys_ros/assets/63952012/1f69091b-dfed-4536-a566-d70a1b9d513e)

#### 2.2.4 Raspberry Pi 4

Connect the 5V output from the step-down converter and inputs to the servo controller (GND, VCC, SCL, SDA), IMU, and Raspberry Pi 4 on a universal circuit board.

![Raspberry Pi Connections](https://github.com/Honazo/Easys_ros/assets/63952012/b0a82e16-43a1-4015-979a-24139510946f)

![More Connections](https://github.com/Honazo/Easys_ros/assets/63952012/78a15f1f-3f58-4925-93b2-888858d24fc6)

![Additional Wiring](https://github.com/Honazo/Easys_ros/assets/63952012/29d9651c-d88c-4d59-90ac-f01ac327607f)

Follow the initial circuit diagram for assembly.

Fit the Raspberry Pi 4 into a case and connect it to the third circuit mount.

![Raspberry Pi Case](https://github.com/Honazo/Easys_ros/assets/63952012/34269222-ebf4-44c3-9311-b2d6781077a9)

Finally, connect the three circuit mounts and the rear flange with bolts and nuts.

![Final Connection](https://github.com/Honazo/Easys_ros/assets/63952012/9838bbc2-b4cb-4a73-a127-9a512312a104)

## 3. Assembly

### 3.1 Thrusters

Insert nuts into the mounting holes of the thruster housing using a soldering iron.

![Insert Nuts](https://github.com/Honazo/Easys_ros/assets/63952012/1861baf3-a66d-47e8-bd0f-77d8b9c01c74)

Secure the thrusters to the thruster mount.

![Thruster Mounting](https://github.com/Honazo/Easys_ros/assets/63952012/9d449b39-f9e1-4558-bf7a-0d0c9b0d5007)

### 3.2 Battery Box

Insert nuts into the four mounting holes on the outside bottom surface of the battery box.

![Battery Box Nuts](https://github.com/Honazo/Easys_ros/assets/63952012/cf0e0b8e-5965-43d1-888c-ce024883fda2)

Drill a Φ12mm hole on the shorter side of the battery box using an electric drill.

![Drill Hole](https://github.com/Honazo/Easys_ros/assets/63952012/c2b8aa42-42ae-479f-bc91-e18f2ae1669e)

Thread the power cable through the cable gland and the hole you've made in the battery box, then loosely secure the cable gland.

Connect a fuse → switch → male T-connector to the end of the power cable inside the battery box.

Connect the Li-Po battery with the T-connector.

Make sure everything fits inside the box, then tighten the cable gland.

![Cable Gland in Battery Box](https://github.com/Honazo/Easys_ros/assets/63952012/131dc1aa-306c-4710-928e-8c223e7bcd98)

Ensure that no debris is trapped as you close the battery box.

![Close Battery Box](https://github.com/Honazo/Easys_ros/assets/63952012/2976fa23-7a3c-416d-972d-06b142818b57)

### 3.3 Outer Frame

The upper external frame has six places, and the lower external frame has two places for inserting nuts for the thruster mounts. Insert nuts at all these points.

![Insert Nuts in Frame](https://github.com/Honazo/Easys_ros/assets/63952012/b9db687a-69b1-49b2-9bd0-87d4a1f0876b)

Connect the lower external frame to the mount for securing the battery box.

Connect the battery box to the mount for securing it.

![Battery Box Mounting](https://github.com/Honazo/Easys_ros/assets/63952012/ba5f1a36-9035-467b-a4fc-b0b332ea0b3c)

Place the acrylic tube on top of the lower frame.

![Acrylic Tube Placement](https://github.com/Honazo/Easys_ros/assets/63952012/0c108d8d-2c67-4864-868a-f563cd321d0d)

Connect the upper frame to the lower frame.
This connection will secure the cylinder by clamping the upper and lower frames together.
Tighten each connection slowly.

![Frame Connection](https://github.com/Honazo/Easys_ros/assets/63952012/4be51ae6-f069-40a8-8e53-995b21937de2)

### 3.4 Waterproof Container

Adhere the acrylic disk to the front flange using acrylic Sunday to fuse them together.

![Acrylic Disk Adhesion](https://github.com/Honazo/Easys_ros/assets/63952012/6c29d233-4286-4bf5-83fa-5abca6695453)

Once the acrylic Sunday has set, secure the webcam to the front flange.

Fit an O-ring onto the front flange.
Apply grease to the O-ring to make it smooth, and gradually stretch and fit it into the groove.

![O-Ring Installation](https://github.com/Honazo/Easys_ros/assets/63952012/177c8d3f-0f5c-4415-b293-3c7a2a3a64d7)

Fit an O-ring onto the rear flange in the same way.

With the USB cable of the webcam disconnected from the Raspberry Pi, fit the front flange to the acrylic tube.
Considerable force may be required. Use grease to smooth the process, pushing any protruding O-rings back in gradually.
Be careful not to trap any debris.

![Flange Installation](https://github.com/Honazo/Easys_ros/assets/63952012/bd57359c-70d5-411c-982f-d3f0c14ae00a)

Connect the USB cable of the webcam to the Raspberry Pi.

Fit the rear flange to the acrylic tube in the same way as the front flange. It's helpful to loosen one cable gland to vent air.

Once the flanges are in place, use cable ties to secure the flanges to the external frame to prevent them from detaching.

Secure the thrusters to the external frame.

![Thruster Final Installation](https://github.com/Honazo/Easys_ros/assets/63952012/96bebd25-191c-46aa-bda7-a0bcc069f749)

## 4. Buoyancy Adjustment

Once sealed, submerge the robot in a shallow water tank such as a bathtub.

If nothing is activated, more than half of the machine should float above the water surface.

Attach fishing weights to the exterior of the machine gradually, adjusting the weight until all four thrusters are submerged.

![Buoyancy Adjustment](https://github.com/Honazo/Easys_ros/assets/63952012/d6c4fd41-da89-4502-bba6-e1e094df7fc8)

## 5. Software Preparation

Setup the environment

Download Easys_ros

### 5.1 Preparing Raspberry Pi

Turn on the machine's power switch

Connect the LAN cable to the PC

Set up the environment

### 5.2 Preparing the Host PC

Launch ros2

Launch

### 5.3 Control Test

