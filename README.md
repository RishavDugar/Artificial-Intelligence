# Artificial-Intelligence

Problem Statement :
Consider a city network where we need to route a set of electric vehicles which may require to be charged during its journey from some source to some destination. Let us assume that we have n cities (v1, v2, . . . , vn) and the distance between cities vi and vj be eij (if two cities are not connected directly then eij = ∞ and eij = eji). Assume that each city has a single charging station which can charge one EV at a time. Consider a set of k EVs namely P1, P2, . . . , Pk. For each EV the following information is provided –

(a) Sr - source node

(b) Dr - destination node

(c) Br - battery charge status initially

(d) cr - charging rate for battery at a charging station (percent charged per unit time)

(e) dr - discharging rate of battery while traveling (distance travel per unit charge)

(f) Mr - maximum battery capacity

(g) sr - average traveling speed (distance per unit time).

Assume that all vehicles start their journey at t = 0 and Pr reaches it destination at t = Tr. We need to route all the vehicles from their respective sources to destinations such that max{Tr} is minimized.

![image](https://user-images.githubusercontent.com/63944682/112748727-5add6280-8fdb-11eb-9a20-9db208bdde94.png)

Follow the Instructions.txt file for installation and user manual.

Read the Report.txt file for the logic and algorithms used.



# Test Case
Node-to-Node Distance

![image](https://user-images.githubusercontent.com/63944682/112759171-76faf700-900f-11eb-8575-c0e8065b9081.png)


Electric Vehicle Details

![image](https://user-images.githubusercontent.com/63944682/113126022-da19a300-9234-11eb-9595-b2264a3c4434.png)

Results obtained

![image](https://user-images.githubusercontent.com/63944682/112759312-06a0a580-9010-11eb-999a-c8a674a534fc.png)

The results can be interpreted using the 'Output Interpretation' in the Instructions.txt 
For the given sample case it does predict the correct results for the given conditions.



