Menu("Choose unknown","Airtime",AT,"Dst Traveled",DR,"Dst at Time",DI,"Time at Dst",TD)

Lbl AT
Input "Delta Y: ",D
Input "Y0 Velocity: ",V
Input "Gravity: ",G
(V^2+2*D*G)^0.5→N
Disp "t is:",(0-V+N)/G,(0-V-N)/G
Stop

Lbl DR
Stop

Lbl DI
Stop

Lbl TD
Stop
