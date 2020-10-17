Menu("Choose unknown","Airtime",AT,"Pjctle Dst",DR,"Dst at Time",DI,"Time at Dst",TD)

Lbl AT
Input "Delta Y: ",D
Input "Y0 Velocity: ",V
Input "Gravity: ",G
(V^2+2*D*G)^0.5→N
Disp "t is: ",(0-V+N)/G,(0-V-N)/G
Stop

Lbl DR
Input "Delta Y: ",D
Input "Y0 Velocity: ",V
Input "X Velocity: ",W
Input "Gravity: ",G
(V^2+2*D*G)^0.5→N
Disp "Dst is: ",(0-V+N)/G,(0-V-N)/G*W
Stop

Lbl DI
Stop

Lbl TD
Stop
