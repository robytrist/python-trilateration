import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox

def trilaterate (p1, p2, p3, r1, r2, r3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    A = 2 * (x2 - x1)
    B = 2 * (y2 - y1)
    C = r1**2 - r2**2 - x1**2 + x2**2 - y1**2 + y2**2
    D = 2 * (x3 - x2)
    E = 2 * (y3 - y2)
    F = r2**2 - r3**2 - x2**2 + x3**2 - y2**2 + y3**2

    x = (C*E - F*B) / (E*A - B*D)
    y = (C*D - A*F) / (B*D - A*E)

    return x, y

# Initial pt coordinates
init_pt_x0, init_pt_y0 = 1, 1
init_pt_x1, init_pt_y1 = 4, 1
init_pt_x2, init_pt_y2 = 2.5,4

# circle properties
init_cir_rad = 2
cir_color = 'green'
cir_alpha = 0.3

# Set up the figure and axis
fig, ax = plt.subplots()
#ax.set_xlim(0, 100)
#ax.set_ylim(0, 100)

# Plot the initial circle
cir0 = plt.Circle((init_pt_x0, init_pt_y0), init_cir_rad, color=cir_color, alpha=cir_alpha)
cir1 = plt.Circle((init_pt_x1, init_pt_y1), init_cir_rad, color=cir_color, alpha=cir_alpha)
cir2 = plt.Circle((init_pt_x2, init_pt_y2), init_cir_rad, color=cir_color, alpha=cir_alpha)
ax.add_patch(cir0)
ax.add_patch(cir1)
ax.add_patch(cir2)

# Plot the initial point
pt0, = ax.plot(init_pt_x0, init_pt_y0, 'yo', markersize=5)
pt1, = ax.plot(init_pt_x1, init_pt_y1, 'yo', markersize=5)
pt2, = ax.plot(init_pt_x2, init_pt_y2, 'yo', markersize=5)

f_pt = trilaterate((init_pt_x0,init_pt_y0),(init_pt_x1,init_pt_y1),(init_pt_x2,init_pt_y2),init_cir_rad,init_cir_rad,init_cir_rad)
Object, = ax.plot(f_pt[0],f_pt[1],'ro',markersize=5)

# Plot r line and value
line0, = plt.plot([init_pt_x0, init_pt_x0 + init_cir_rad], [init_pt_y0, init_pt_y0],'r:')
line1, = plt.plot([init_pt_x1, init_pt_x1 + init_cir_rad], [init_pt_y1, init_pt_y1],'r:')
line2, = plt.plot([init_pt_x2, init_pt_x2 + init_cir_rad], [init_pt_y2, init_pt_y2],'r:')

# Display the initial radius value
radius0_text = ax.text(init_pt_x0 + init_cir_rad / 2, init_pt_y0 ,
                      f"r₁: {init_cir_rad:.1f}",ha='center',va='top', fontsize=7, color='black')
radius1_text = ax.text(init_pt_x1 + init_cir_rad / 2, init_pt_y1,
                      f"r₂: {init_cir_rad:.1f}",ha='center',va='top', fontsize=7, color='black')
radius2_text = ax.text(init_pt_x2 + init_cir_rad / 2, init_pt_y2,
                      f"r₃: {init_cir_rad:.1f}",ha='center',va='top', fontsize=7, color='black')
Station0_text = ax.text(init_pt_x0, init_pt_y0,
                      "Station 1",ha='right',va='bottom', fontsize=9, color='red')
Station1_text = ax.text(init_pt_x1, init_pt_y1,
                      "Station 2",ha='right',va='bottom', fontsize=9, color='red')
Station2_text = ax.text(init_pt_x2, init_pt_y2,
                      "Station 3",ha='right',va='bottom', fontsize=9, color='red')
Object_text = ax.text(f_pt[0],f_pt[1], "Object Position",ha='left',va='bottom',fontsize=9,color='black')

# Text box positions
text_x0_ax = plt.axes([0.15, 0.1, 0.15, 0.03], facecolor='lightgoldenrodyellow')
text_y0_ax = plt.axes([0.15, 0.06, 0.15, 0.03], facecolor='lightgoldenrodyellow')
text_radius0_ax = plt.axes([0.15, 0.02, 0.15, 0.03], facecolor='lightgoldenrodyellow')
text_x1_ax = plt.axes([0.35, 0.1, 0.15, 0.03], facecolor='lightgoldenrodyellow')
text_y1_ax = plt.axes([0.35, 0.06, 0.15, 0.03], facecolor='lightgoldenrodyellow')
text_radius1_ax = plt.axes([0.35, 0.02, 0.15, 0.03], facecolor='lightgoldenrodyellow')
text_x2_ax = plt.axes([0.55, 0.1, 0.15, 0.03], facecolor='lightgoldenrodyellow')
text_y2_ax = plt.axes([0.55, 0.06, 0.15, 0.03], facecolor='lightgoldenrodyellow')
text_radius2_ax = plt.axes([0.55, 0.02, 0.15, 0.03], facecolor='lightgoldenrodyellow')

# Create the text boxes for X, Y coordinates, and the radius
text_x0 = TextBox(text_x0_ax, 'X₁', initial="{:.1f}".format(init_pt_x0))
text_y0 = TextBox(text_y0_ax, 'Y₁', initial="{:.1f}".format(init_pt_y0))
text_radius0 = TextBox(text_radius0_ax, 'r₁', initial="{:.1f}".format(init_cir_rad))
text_x1 = TextBox(text_x1_ax, 'X₂', initial="{:.1f}".format(init_pt_x1))
text_y1 = TextBox(text_y1_ax, 'Y₂', initial="{:.1f}".format(init_pt_y1))
text_radius1 = TextBox(text_radius1_ax, 'r₂', initial="{:.1f}".format(init_cir_rad))
text_x2 = TextBox(text_x2_ax, 'X₃', initial="{:.1f}".format(init_pt_x2))
text_y2 = TextBox(text_y2_ax, 'Y₃', initial="{:.1f}".format(init_pt_y2))
text_radius2 = TextBox(text_radius2_ax, 'r₃', initial="{:.1f}".format(init_cir_rad))

def update(val):
    """Update the circle, point, line, and radius text based on the text box values"""
    try:
        pt_x0 = float(text_x0.text)
        pt_y0 = float(text_y0.text)
        rad0 = float(text_radius0.text)
        pt_x1 = float(text_x1.text)
        pt_y1 = float(text_y1.text)
        rad1 = float(text_radius1.text)
        pt_x2 = float(text_x2.text)
        pt_y2 = float(text_y2.text)
        rad2 = float(text_radius2.text)
        

        pt0.set_data(pt_x0, pt_y0)
        cir0.set_center((pt_x0, pt_y0))
        cir0.set_radius(rad0)
        pt1.set_data(pt_x1, pt_y1)
        cir1.set_center((pt_x1, pt_y1))
        cir1.set_radius(rad1)
        pt2.set_data(pt_x2, pt_y2)
        cir2.set_center((pt_x2, pt_y2))
        cir2.set_radius(rad2)


        f_pt0 = trilaterate((pt_x0,pt_y0),(pt_x1,pt_y1),(pt_x2,pt_y2),rad0,rad1,rad2)
        Object.set_data(f_pt0[0],f_pt0[1])


        line0.set_data([pt_x0, pt_x0 + rad0], [pt_y0, pt_y0])
        radius0_text.set_text(f"r1: {rad0:.2f}")
        radius0_text.set_position((pt_x0 + rad0 / 2, pt_y0 - 5))
        line1.set_data([pt_x1, pt_x1 + rad1], [pt_y1, pt_y1])
        radius1_text.set_text(f"r2: {rad1:.2f}")
        radius1_text.set_position((pt_x1 + rad1 / 2, pt_y1 - 5))
        line2.set_data([pt_x2, pt_x2 + rad2], [pt_y2, pt_y2])
        radius2_text.set_text(f"r3: {rad2:.2f}")
        radius2_text.set_position((pt_x2 + rad2 / 2, pt_y2 - 5))

        # p0 = (pt_x0,pt_y0)
        # p1 = (pt_x1,pt_y1)
        # p2 = (pt_x2,pt_y2)

        

        fig.canvas.draw_idle()
    except ValueError:
        pass

# Connect the text boxes to the update function
text_x0.on_submit(update)
text_y0.on_submit(update)
text_radius0.on_submit(update)
text_x1.on_submit(update)
text_y1.on_submit(update)
text_radius1.on_submit(update)
text_x2.on_submit(update)
text_y2.on_submit(update)
text_radius2.on_submit(update)

plt.show()

