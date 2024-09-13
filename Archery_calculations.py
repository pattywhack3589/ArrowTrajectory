# Import packages
import math
import numpy as np
import matplotlib.pyplot as plt
import random
import seaborn as sns

sns.set_style('whitegrid')

# Input bow specifications

draw_length = 27.5  # inches
draw_weight = 60  # pounds
ATA_rating = 332  # feet per second
IBO_rating = 324  # feet per second
Average_speed = (ATA_rating + IBO_rating) / 2

# For every inch of draw length under 30″, subtract 10 fps, every inch over 30″ add 10 fps.
draw_adjust = (draw_length - 30) * 10  # feet per second

# For every 3 grains of weight on the bow string, subtract 1 fps.
kisser_weight = 0  # grains
nosebutton_weight = 15  # grains
peep_weight = 20  # grains
dloop_weight = 10  # grains
string_adjust = (kisser_weight + nosebutton_weight + peep_weight + dloop_weight) / -3  # feet per second

# Input Arrow 1 specifications

A1_gpi = 8.82  # grains per inch
A1_length = 27.5  # inches
A1_insert = 125  # grains
A1_head = 100  # grains
A1_fletching = 6  # grains each
A1_nvanes = 3  # number of vanes
A1_wrap = 0  # grains
A1_nock = 7  # grains
A1_weight = A1_gpi * A1_length + A1_insert + A1_head + A1_fletching * A1_nvanes + A1_wrap + A1_nock
print("Arrow 1 weighs " + str(round(A1_weight, 0)) + " grains")

# Arrow 1 Speed
# For every 3 grains of total arrow weight above 5 grains per pound of draw weight, subtract 1 fps.
Idealarrowweight = 5 * draw_weight
A1_weightadjust = (Idealarrowweight - A1_weight) / 3
A1_speed = Average_speed + draw_adjust + string_adjust + A1_weightadjust
print("Arrow 1 travels " + str(round(A1_speed, 0)) + " feet per second")

# Input Arrow 2 specifications

A2_gpi = 6.9  # grains per inch
A2_length = 26  # inches
A2_insert = 14  # grains
A2_head = 100  # grains
A2_fletching = 6  # grains each
A2_nvanes = 3  # number of vanes
A2_wrap = 0  # grains
A2_nock = 7  # grains
A2_weight = A2_gpi * A2_length + A2_insert + A2_head + A2_fletching * A2_nvanes + A2_wrap + A2_nock
print("Arrow 2 weighs " + str(round(A2_weight, 0)) + " grains")

# Arrow 2 Speed
# For every 3 grains of total arrow weight above 5 grains per pound of draw weight, subtract 1 fps.
Idealarrowweight = 5 * draw_weight
A2_weightadjust = (Idealarrowweight - A2_weight) / 3
A2_speed = Average_speed + draw_adjust + string_adjust + A2_weightadjust
print("Arrow 2 travels " + str(round(A2_speed, 0)) + " feet per second")

# Specify target estimation error distribution
est_error_mean = 1  # yards
est_error_stddev = 2  # yards
num_shots = 1000

est_error_dist = np.random.normal(est_error_mean, est_error_stddev, num_shots).round(2)
# print(est_error_dist.shape)

# plt.hist(est_error_dist, density=True, bins=30)  # density=False would make counts
# plt.ylabel('Probability')
# plt.xlabel('Data');
# plt.show()

# Specify vertical shot error distribution
vert_error_mean = 0  # degrees
vert_error_stddev = 0.12  # degrees

vert_error_dist = np.random.normal(vert_error_mean, vert_error_stddev, num_shots).round(2)
# print(vert_error_dist.shape)

# plt.hist(vert_error_dist, density=True, bins=30)  # density=False would make counts
# plt.ylabel('Probability')
# plt.xlabel('Data');
# plt.show()

# Specify horizontal shot error distribution
horz_error_mean = 0  # degrees
horz_error_stddev = 0.08  # degrees

horz_error_dist = np.random.normal(horz_error_mean, horz_error_stddev, num_shots).round(2)
# print(horz_error_dist.shape)

# plt.hist(horz_error_dist, density=True, bins=30)  # density=False would make counts
# plt.ylabel('Probability')
# plt.xlabel('Data');
# plt.show()

# Specify target distance
targ_dist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]  # yards

for a in targ_dist:

    # Enter trajectory equations for Arrow 1
    A1_dx = 0  # initial distance yards
    gravity = 32.2  # feet/second^2
    yds_ft = 3  # feet per yard
    pi = math.pi
    deg_rad = pi / 180
    rad_deg = 180 / pi
    A1_opt_traj = (np.arcsin((a * yds_ft * gravity) / (A1_speed ** 2)) / 2) * rad_deg
    A1_theta = A1_opt_traj
    A1_flt_t = (2 * A1_speed * math.sin(A1_theta * deg_rad)) / gravity
    print("Arrow 1's time of flight at " + str(a) + " yards is " + str(round(A1_flt_t, 2)) + " seconds")

    A1_traj = []
    A1_xvalues = []
    while A1_dx <= a:
        A1_y = ((math.tan(A1_theta * deg_rad) * A1_dx * yds_ft) - (gravity * ((A1_dx * yds_ft) ** 2)) / (
                    2 * (A1_speed ** 2) * ((math.cos(A1_theta * deg_rad)) ** 2))) * 12
        A1_traj.append(A1_y)
        A1_xvalues.append(A1_dx)
        A1_dx = A1_dx + 0.5

    A1_x = np.asarray(A1_xvalues)
    A1_y = np.asarray(A1_traj)

    # Enter trajectory equations for Arrow 2
    A2_dx = 0  # initial distance yards
    A2_opt_traj = (np.arcsin((a * yds_ft * gravity) / (A2_speed ** 2)) / 2) * rad_deg
    A2_theta = A2_opt_traj
    A2_flt_t = (2 * A2_speed * math.sin(A2_theta * deg_rad)) / gravity
    print("Arrow 2's time of flight at " + str(a) + " yards is " + str(round(A2_flt_t, 2)) + " seconds")

    A2_traj = []
    A2_xvalues = []
    while A2_dx <= a:
        A2_y = ((math.tan(A2_theta * deg_rad) * A2_dx * yds_ft) - (gravity * ((A2_dx * yds_ft) ** 2)) / (
                    2 * (A2_speed ** 2) * ((math.cos(A2_theta * deg_rad)) ** 2))) * 12
        A2_traj.append(A2_y)
        A2_xvalues.append(A2_dx)
        A2_dx = A2_dx + 0.5

    A2_x = np.asarray(A2_xvalues)
    A2_y = np.asarray(A2_traj)

    plt.plot(A1_x, A1_y, label="Arrow 1")
    plt.plot(A2_x, A2_y, label="Arrow 2")
    plt.title("Arrow 1 vs Arrow 2 Flight at " + str(a) + " Yards")
    plt.xlabel('Shot Distance (Yards)')
    plt.ylabel('Height (inches)')
    plt.legend(loc="upper right")
    plt.show()

    # Calculate maximum arrow flight heights
    print("Arrow 1's maximum height is " + str(round(max(A1_traj), 2)) + " inches for a target distance of " + str(
        a) + " yards")
    print("Arrow 2's maximum height is " + str(round(max(A2_traj), 2)) + " inches for a target distance of " + str(
        a) + " yards")

    # Calculate trajectory difference
    if A1_traj > A2_traj:
        traj_diff = round(max(A1_traj) - max(A2_traj), 2)
        print("Arrow 2's maximum height is " + str(traj_diff) + " inches flatter than Arrow 1")
    elif A1_traj < A2_traj:
        traj_diff = round(max(A2_traj) - max(A1_traj), 2)
        print("Arrow 1's maximum height is " + str(traj_diff) + " inches flatter than Arrow 2")

# declare number of simulation shots
its = 1000

# define minimum and maximum shot distances
min1 = 10  # yds
max1 = 50  # yds

# Create random target distances for both arrows
targ_dist_list = []  # yards
for a in range(0, its):
    b = random.randint(min1, max1)
    targ_dist_list.append(b)

targ_dist_array = np.asarray(targ_dist_list)
print('Target Average Distance = ' + str(round(np.average(targ_dist_array), 1)) + ' yards')

# Adjust exact yardage to estimated yardage
estimated_ydg = targ_dist_array + est_error_dist
print('Estimated Average Target Distance =' + str(round(np.average(estimated_ydg), 1)) + 'yards')

# calculate shot angle for Arrow 1 distances
A1_shot_ang = []
for e in estimated_ydg:
    theta_1 = (np.arcsin((e * 3 * gravity) / (A1_speed ** 2)) / 2)
    A1_shot_ang.append(theta_1)

# create array for horizontal shot impacts
horz_imp = []
for k, j in zip(horz_error_dist, targ_dist_array):
    l = j * 3 * 12 * math.tan(k * deg_rad)  # listed in inches
    horz_imp.append(l)

A1_adjusted_angle = np.asarray(A1_shot_ang) + (vert_error_dist * deg_rad)

# calculate estimated distance shot impact from target point (0,0) coordinate
A1_sim_impacts = []
for u, t in zip(targ_dist_array, A1_adjusted_angle):
    A1_y_imp = (((math.tan(t)) * u * 3) - (
                (gravity * ((u * 3) ** 2)) / (2 * (A1_speed ** 2) * ((math.cos(t)) ** 2)))) * 12
    A1_sim_impacts.append(A1_y_imp)

plt.scatter(horz_imp, A1_sim_impacts, label="Arrow 1")

# ARROW 2

# calculate shot angle for Arrow 2 estimated distances
A2_shot_ang = []
for e in estimated_ydg:
    theta_2 = (np.arcsin((e * 3 * gravity) / (A2_speed ** 2)) / 2)
    A2_shot_ang.append(theta_2)

# Adjust vertical shot angle array
A2_adjusted_angle = np.asarray(A2_shot_ang) + (vert_error_dist * deg_rad)

# calculate estimated distance shot impact from target point (0,0) coordinate
A2_sim_impacts = []
for m, n in zip(targ_dist_array, A2_adjusted_angle):
    A2_y_imp = (((math.tan(n)) * m * 3) - (
                (gravity * ((m * 3) ** 2)) / (2 * (A2_speed ** 2) * ((math.cos(n)) ** 2)))) * 12
    A2_sim_impacts.append(A2_y_imp)

plt.scatter(horz_imp, A2_sim_impacts, label="Arrow 2")

# Specify plot title, labels, and legend
plt.title("Arrow 1 vs Arrow 2 Target Impacts at Estimated Distances; " + str(its) + " shots each")
plt.xlabel('Horizontal Impact (inches)')
plt.ylabel('Vertical Impact (inches)')
plt.legend(loc="upper right")
plt.show()

print("Arrow 1 is off target an average of " + str(round(np.average(A1_sim_impacts), 2)) + " inches vertically")

if abs(np.max(A1_sim_impacts)) > abs(np.min(A1_sim_impacts)):
    print("Arrow 1's maximum vertical distance from bullseye is " + str(
        round(abs(np.max(A1_sim_impacts)), 2)) + " inches")
else:
    print("Arrow 1's maximum vertical distance from bullseye is " + str(
        round(abs(np.min(A1_sim_impacts)), 2)) + " inches")

print("Arrow 2 is off target an average of " + str(round(np.average(A2_sim_impacts), 2)) + " inches vertically ")
if abs(np.max(A2_sim_impacts)) > abs(np.min(A2_sim_impacts)):
    print("Arrow 2's maximum vertical distance from bullseye is " + str(
        round(abs(np.max(A2_sim_impacts)), 2)) + " inches")
else:
    print("Arrow 2's maximum vertical distance from bullseye is " + str(
        round(abs(np.min(A2_sim_impacts)), 2)) + " inches")

# Calculate scores for each arrow

# Specify scoring ring sizes
ten_dia = 4 / 2.54  # inches
nine_dia = 8 / 2.54  # inches
eight_dia = 12 / 2.54  # inches
seven_dia = 16 / 2.54  # inches
six_dia = 20 / 2.54  # inches
five_dia = 24 / 2.54  # inches
four_dia = 28 / 2.54  # inches
three_dia = 32 / 2.54  # inches
two_dia = 36 / 2.54  # inches
one_dia = 40 / 2.54  # inches

# Calculate distance from (0,0) for each impact for both arrows
A1_dist_from_org = []
for w, x in zip(horz_imp, A1_sim_impacts):
    A1_org = math.sqrt((w ** 2) + (x ** 2))
    A1_dist_from_org.append(A1_org)

A2_dist_from_org = []
for y, z in zip(horz_imp, A2_sim_impacts):
    A2_org = math.sqrt((y ** 2) + (z ** 2))
    A2_dist_from_org.append(A2_org)

A1_shot_score = []

for q in A1_dist_from_org:
    if abs(q) <= ten_dia:
        r = 10
    elif abs(q) <= nine_dia and abs(q) > ten_dia:
        r = 9
    elif abs(q) <= eight_dia and abs(q) > nine_dia:
        r = 8
    elif abs(q) <= seven_dia and abs(q) > eight_dia:
        r = 7
    elif abs(q) <= six_dia and abs(q) > seven_dia:
        r = 6
    elif abs(q) <= five_dia and abs(q) > six_dia:
        r = 5
    elif abs(q) <= four_dia and abs(q) > five_dia:
        r = 4
    elif abs(q) <= three_dia and abs(q) > four_dia:
        r = 3
    elif abs(q) <= two_dia and abs(q) > three_dia:
        r = 2
    elif abs(q) <= one_dia and abs(q) > two_dia:
        r = 1
    else:
        r = 0
    A1_shot_score.append(r)

print("Arrow 1's average score is " + str(round(np.sum(A1_shot_score) / 33.33, 0)))

A2_shot_score = []

for o in A2_dist_from_org:
    if abs(o) <= ten_dia:
        p = 10
    elif abs(o) <= nine_dia and abs(o) > ten_dia:
        p = 9
    elif abs(o) <= eight_dia and abs(o) > nine_dia:
        p = 8
    elif abs(o) <= seven_dia and abs(o) > eight_dia:
        p = 7
    elif abs(o) <= six_dia and abs(o) > seven_dia:
        p = 6
    elif abs(o) <= five_dia and abs(o) > six_dia:
        p = 5
    elif abs(o) <= four_dia and abs(o) > five_dia:
        p = 4
    elif abs(o) <= three_dia and abs(o) > four_dia:
        p = 3
    elif abs(o) <= two_dia and abs(o) > three_dia:
        p = 2
    elif abs(o) <= one_dia and abs(o) > two_dia:
        p = 1
    else:
        p = 0
    A2_shot_score.append(p)

print("Arrow 2's average score is " + str(round(np.sum(A2_shot_score) / 33.33, 0)))