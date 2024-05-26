from manim import *

class NewtonRaphson(Scene):
    def construct(self):
        # Define the function and its derivative
        def func(x):
            return x**4 - 4*x**3 + 6*x**2 - 4*x + 1  # Example function with higher curves

        def dfunc(x):
            return 4*x**3 - 12*x**2 + 12*x - 4  # Derivative of the function


        # Initial guess
        x0 = 3.0
        iterations = 4

        # Axes
        axes = Axes(
            x_range=[0, 5, 0.5],
            y_range=[-4, 16, 2],
            axis_config={"include_numbers": True}
        )

        # Function graph
        graph = axes.plot(func, color=BLUE)
        graph_label = axes.get_graph_label(graph, label='f(x)')

        # Adding the axes and graph to the scene
        self.play(Create(axes), Create(graph), Write(graph_label))

        vert_line = self.get_vertical_line(axes, x0)
        self.play(Create(vert_line), run_time=1)
        # Perform Newton-Raphson iterations
        for _ in range(iterations):
            # Calculate the value of the function and its derivative at x0
            y0 = func(x0)
            dy0 = dfunc(x0)

            # Plot the current point
            dot = Dot(axes.c2p(x0, y0), color=RED)
            self.play(FadeIn(dot), run_time=0.5)

            # Draw the tangent line at the current point
            tangent_line = self.get_tangent_line(axes, func, dfunc, x0, x_range=[0, 4])
            self.play(Create(tangent_line), run_time=1)

            # Update x0 using Newton-Raphson formula
            x1 = x0 - y0 / dy0

            # Draw a vertical line from the tangent line to the x-axis
            vert_line = self.get_vertical_line(axes, x1)
            self.play(Create(vert_line), run_time=1)

            # Update x0 for the next iteration
            x0 = x1

            # Move dot to the new point on the x-axis
            new_dot = Dot(axes.c2p(x0, 0), color=GREEN)
            self.play(Transform(dot, new_dot), run_time=0.5)
            self.remove(vert_line)
            self.play(FadeOut(tangent_line))

        self.wait(3)

    def get_tangent_line(self, axes, func, dfunc, x, x_range):
        slope = dfunc(x)
        y_intercept = func(x) - slope * x
        tangent_func = lambda t: slope * t + y_intercept

        return axes.plot(tangent_func, x_range=x_range, color=GREEN)

    def get_vertical_line(self, axes, x):
        line = DashedLine(
            start=axes.c2p(x, 0),
            end=axes.c2p(x, axes.y_range[1]),
            stroke_width=2,
            stroke_color=YELLOW,
            stroke_opacity=0.7
        )
        return line
