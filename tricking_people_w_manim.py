import manim as m
import numpy as np


class VecHelper:
    '''
    Пример использования:
    v = VecHelper()
    v[1, 2, 3]  # np.ndarray([1, 2, 3])
    '''
    def __getitem__(self, key):
        '''Возвращает вектор по координатам'''
        if len(key) == 3:
            return np.array(list(key))
        elif len(key) == 2:
            return np.array(list(key) + [0])


def abs2d(x, y):
    return np.sqrt(x ** 2 + y ** 2)


class Scene_01(m.Scene):
    def construct(self):
        v = VecHelper()

    # Intro
        self.wait(0.5)
        text_intro_01 = m.Text('Дурим людей с помощью manim', font='CMU Serif')
        text_intro_01.shift(m.UP)
        self.play(m.Write(text_intro_01))
        self.wait(0.2)

        line_intro_01 = m.Line(v[-5, 1, 0], v[-0.8, 1, 0], color=m.RED)
        self.play(m.Write(line_intro_01))
        self.wait(0.2)

        text_intro_02 = m.Text('   Показываем\nматематические\n  парадоксы :)', font='CMU Serif').scale(0.8)
        text_intro_02.next_to(text_intro_01, direction=m.DOWN, aligned_edge=m.LEFT)
        self.play(m.Write(text_intro_02))
        self.wait()

        self.play(m.FadeOut(text_intro_01, line_intro_01, text_intro_02))
    
    # Paradox 1
    ### intro
        text_par1_01_a = m.Text(
            '(1) Окружность — это правильный многоугольник\nс бесконечным числом углов.',
            font='CMU Serif'
        ).scale(0.8)
        text_par1_01_b = text_par1_01_a.copy().scale(0.8)
        text_par1_01_c = text_par1_01_b.copy().to_corner(m.UL)

        self.play(m.Write(text_par1_01_a, run_time=2))
        self.play(m.ReplacementTransform(text_par1_01_a, text_par1_01_b), run_time=0.6)
        self.play(m.ReplacementTransform(text_par1_01_b, text_par1_01_c), run_time=0.6)

        self.wait(0.3)

    ### data
        par1_circles_SHIFT = 0.5 * m.DOWN

        circle_par1_01 = m.Circle(2, m.RED).shift(par1_circles_SHIFT)

        text_par1_data_01 = m.Text('Число сторон: ', font='CMU Serif'
        ).scale(0.5).next_to(text_par1_01_c, direction=m.DOWN, aligned_edge=m.LEFT)
        text_par1_data_02 = m.Text('Периметр: ', font='CMU Serif'
        ).scale(0.5).next_to(text_par1_data_01, direction=m.DOWN, aligned_edge=m.LEFT)
        text_par1_data_03 = m.Text('Площадь: ', font='CMU Serif'
        ).scale(0.5).next_to(text_par1_data_02, direction=m.DOWN, aligned_edge=m.LEFT)

        self.play(m.AnimationGroup(
            m.GrowFromCenter(circle_par1_01),
            m.FadeIn(text_par1_data_01, run_time=0.5),
            m.FadeIn(text_par1_data_02, run_time=0.5),
            m.FadeIn(text_par1_data_03, run_time=0.5),
            lag_ratio=0.25
        ))
    
    ### circles
        dot_par1_01 = m.Dot(color=m.YELLOW).shift(par1_circles_SHIFT)
        text_par1_data_01_value = m.Text('0', color=m.YELLOW, font='CMU Serif'
        ).scale(0.5).next_to(text_par1_data_01)
        text_par1_data_02_value = m.Text('нет', color=m.YELLOW, font='CMU Serif'
        ).scale(0.5).next_to(text_par1_data_02)
        text_par1_data_03_value = m.Text('нет', color=m.YELLOW, font='CMU Serif'
        ).scale(0.5).next_to(text_par1_data_03)
        self.play(
            m.FadeIn(dot_par1_01),
            m.FadeIn(text_par1_data_01_value),
            m.FadeIn(text_par1_data_02_value),
            m.FadeIn(text_par1_data_03_value),
            run_time=1
        )

        def Par1_circles_rewrite_and_add_data(d1, d2, d3):
            '''d1: str, d2: str, d3: str'''
            nonlocal self, text_par1_data_01_value, text_par1_data_02_value, text_par1_data_03_value
            self.remove(text_par1_data_01_value, text_par1_data_02_value, text_par1_data_03_value)
            text_par1_data_01_value = m.Text(d1, color=m.YELLOW, font='CMU Serif'
            ).scale(0.5).next_to(text_par1_data_01)
            text_par1_data_02_value = m.Text(d2, color=m.YELLOW, font='CMU Serif'
            ).scale(0.5).next_to(text_par1_data_02)
            text_par1_data_03_value = m.Text(d3, color=m.YELLOW, font='CMU Serif'
            ).scale(0.5).next_to(text_par1_data_03)
            self.add(text_par1_data_01_value, text_par1_data_02_value, text_par1_data_03_value)
        
        self.wait(2)

        line_par1_01 = m.Line(v[-2, -0.5, 0], v[2, -0.5, 0], color=m.YELLOW)
        Par1_circles_rewrite_and_add_data('1', '1', 'нет')
        self.play(m.ReplacementTransform(dot_par1_01, line_par1_01), run_time=0.8)
        self.wait(0.8)

        polygon_par1_01 = m.RegularPolygon(3, radius=2, color=m.YELLOW).shift(par1_circles_SHIFT)
        Par1_circles_rewrite_and_add_data(
            '3',
            str(6 * np.sin(np.pi / 3)),
            str(3 / 2 * np.sin(2 * np.pi / 3))
        )
        self.play(m.ReplacementTransform(line_par1_01, polygon_par1_01), run_time=0.8)
        self.wait(0.8)

        for n_edges in range(4, 10 + 1):
            curr_run_time = 0.8 - 0.07 * (n_edges - 3) if n_edges <= 16 else 0.2

            polygon_par1_01_delta = m.RegularPolygon(n_edges, radius=2, color=m.YELLOW,
            ).shift(par1_circles_SHIFT)
            # start_angle=(1 - n_edges % 2) * np.pi / n_edges
            Par1_circles_rewrite_and_add_data(
                str(n_edges),
                str(n_edges * 2 * np.sin(np.pi / n_edges))[:6],
                str(n_edges / 2 * np.sin(2 * np.pi / n_edges))[:6]
            )
            self.play(m.ReplacementTransform(polygon_par1_01, polygon_par1_01_delta),
                      run_time=curr_run_time)
            self.wait(curr_run_time)
            polygon_par1_01 = polygon_par1_01_delta
        
        for n_edges in range(10, 30 + 1):
            curr_run_time = 0.15

            polygon_par1_01_delta = m.RegularPolygon(n_edges, radius=2, color=m.YELLOW,
            ).shift(par1_circles_SHIFT)
            # start_angle=(1 - n_edges % 2) * np.pi / n_edges
            Par1_circles_rewrite_and_add_data(
                str(n_edges),
                str(n_edges * 2 * np.sin(np.pi / n_edges))[:6],
                str(n_edges / 2 * np.sin(2 * np.pi / n_edges))[:6]
            )
            self.remove(polygon_par1_01)
            self.add(polygon_par1_01_delta)
            self.wait(2 * curr_run_time)
            polygon_par1_01 = polygon_par1_01_delta
        
        for n_edges in list(range(30, 100 + 1, 10)) + [200, 300, 400, 500]:
            curr_run_time = 0.27

            polygon_par1_01_delta = m.RegularPolygon(n_edges, radius=2, color=m.YELLOW,
            ).shift(par1_circles_SHIFT)
            # start_angle=(1 - n_edges % 2) * np.pi / n_edges
            Par1_circles_rewrite_and_add_data(
                str(n_edges),
                str(n_edges * 2 * np.sin(np.pi / n_edges))[:6],
                str(n_edges / 2 * np.sin(2 * np.pi / n_edges))[:6]
            )
            self.remove(polygon_par1_01)
            self.add(polygon_par1_01_delta)
            self.wait(2 * curr_run_time)
            polygon_par1_01 = polygon_par1_01_delta
        
        self.wait(0.5)
        
        text_par1_02 = m.MathTex(r'\approx\ 2\pi \cdot 1', color=m.RED
        ).scale(0.64).next_to(text_par1_data_02_value)
        text_par1_03 = m.MathTex(r'\approx\ \pi \cdot 1^2', color=m.RED
        ).scale(0.64).next_to(text_par1_data_03_value)

        self.play(
            m.FadeIn(text_par1_02),
            m.FadeIn(text_par1_03)
        )

        self.wait(4)

        self.play(m.FadeOut(
            text_par1_01_c, text_par1_02, text_par1_03,
            text_par1_data_01, text_par1_data_02, text_par1_data_03,
            text_par1_data_01_value, text_par1_data_02_value, text_par1_data_03_value,
            polygon_par1_01_delta, circle_par1_01
        ), run_time = 2)

        self.wait(2)

    # Paradox 2
    ### intro
        text_par2_01_a = m.Text(
            '(2) Прямая — это окружность бесконечного радиуса.', font='CMU Serif'
        ).scale(0.8)
        text_par2_01_b = text_par2_01_a.copy().scale(0.8)
        text_par2_01 = text_par2_01_b.copy().to_edge(m.UP)

        self.play(m.Write(text_par2_01_a, run_time=2))
        self.play(m.ReplacementTransform(text_par2_01_a, text_par2_01_b), run_time=0.6)
        self.play(m.ReplacementTransform(text_par2_01_b, text_par2_01), run_time=0.6)
        self.wait(0.5)

    ### circles
        tracker_par2_01 = m.ValueTracker(1.0001)
        line_par2_01 = m.Line(v[-8, 1, 0], v[8, 1, 0], color=m.YELLOW)
        text_par2_02 = m.Text('    Радиус: ', font='CMU Serif'
        ).scale(0.64).next_to(text_par2_01, direction=m.DOWN, aligned_edge=m.LEFT)

        dot_par2_01 = m.always_redraw(lambda:
            m.Dot(v[0, 1 - tracker_par2_01.get_value(), 0])
        )

        def circle_par2_01_lambda():
            nonlocal tracker_par2_01
            tracker_value = tracker_par2_01.get_value()
            return m.Circle(tracker_value).shift(v[0, 1 - tracker_value, 0])
        circle_par2_01 = m.always_redraw(circle_par2_01_lambda)

        def text_par2_data_01_lambda():
            nonlocal tracker_par2_01
            str_tracker_value = str(tracker_par2_01.get_value())
            finish_index = str_tracker_value.index('.') + 3
            return m.Text(str_tracker_value[:finish_index], font='CMU Serif', color=m.RED
            ).scale(0.64).next_to(text_par2_02)
        text_par2_data_01 = m.always_redraw(text_par2_data_01_lambda)

        self.play(m.Write(line_par2_01), run_time=0.8)
        self.play(m.FadeIn(dot_par2_01), run_time=0.4)
        self.play(m.Write(circle_par2_01), run_time=0.8)
        self.play(m.Write(text_par2_02), run_time=0.7)
        self.play(m.Write(text_par2_data_01), run_time=0.1)

        self.wait()

        self.play(tracker_par2_01.animate.set_value(2.0001), run_time=2)
        self.wait(0.5)
        self.play(tracker_par2_01.animate.set_value(5.0001), run_time=2)
        self.wait(0.5)
        self.play(tracker_par2_01.animate.set_value(100.0001), run_time=2)
        self.wait(0.5)
        self.play(tracker_par2_01.animate.set_value(10000.0001), run_time=2)
        self.wait(4)

        self.play(m.FadeOut(
            text_par2_01, text_par2_02, text_par2_data_01,
            line_par2_01, dot_par2_01, circle_par2_01
        ))

        self.wait(2)

    # Paradox 3
    ### intro
        text_par3_01_a = m.MathTex(r'(3)\ \pi = 4')
        text_par3_01_b = text_par3_01_a.copy().scale(0.8)
        text_par3_01 = text_par3_01_b.copy().to_corner(m.UL)

        self.play(m.Write(text_par3_01_a))
        self.play(m.ReplacementTransform(text_par3_01_a, text_par3_01_b), run_time=0.6)
        self.play(m.ReplacementTransform(text_par3_01_b, text_par3_01), run_time=0.6)

        self.wait(0.5)

    ### circles
        circle_par3_01 = m.Circle(2, color=m.RED)
        square_par3_01 = m.Square(4, color=m.YELLOW)

        self.play(m.AnimationGroup(
                m.FadeIn(circle_par3_01, scale=0),
                m.Write(square_par3_01),
                lag_ratio=0.4
            ),
            run_time=1.2
        )

        self.wait(0.4)

        text_par3_02 = m.Text('Периметр: 8', color=m.YELLOW, font='CMU Serif'
        ).scale(0.8).next_to(circle_par3_01, direction=m.UP)
        text_par3_03_1 = m.Text('Периметр: ', color=m.RED, font='CMU Serif'
        ).scale(0.8).next_to(circle_par3_01, direction=m.RIGHT)
        text_par3_03_2 = m.MathTex(r'2\pi', color=m.RED
        ).next_to(text_par3_03_1)
        
        self.play(m.TransformFromCopy(square_par3_01, text_par3_02), run_time=1.5)
        self.play(
            m.TransformFromCopy(circle_par3_01, text_par3_03_1),
            m.TransformFromCopy(circle_par3_01, text_par3_03_2),
            run_time=1.5
        )

        par3_corner_points = [
            v[-2, -2], v[-2, 2], v[2, 2], v[2, -2]
        ]
        par3_lines = [
            m.Line(
                par3_corner_points[i], 
                par3_corner_points[(i + 1) % len(par3_corner_points)],
                color = m.YELLOW
            )
            for i in range(len(par3_corner_points))
        ]
        self.add(*par3_lines)
        self.remove(square_par3_01)

        self.wait(1)

        for times in range(6):
            par3_corner_points_delta = []
            for i in range(len(par3_corner_points)):
                curr_x = par3_corner_points[i][0]
                curr_y = par3_corner_points[i][1]
                if curr_x ** 2 + curr_y ** 2 > 4.001:
                    curr_abs = abs2d(curr_x, curr_y)
                    if curr_x * curr_y > 0:
                        new_x = 2 * curr_x / curr_abs
                        new_y = par3_corner_points[(i - 1) % len(par3_corner_points)][1]
                        par3_corner_points_delta.append(v[new_x, new_y])
                        new_y = 2 * curr_y / curr_abs
                        par3_corner_points_delta.append(v[new_x, new_y])
                        new_x = par3_corner_points[(i + 1) % len(par3_corner_points)][0]
                        par3_corner_points_delta.append(v[new_x, new_y])
                    else:
                        new_x = par3_corner_points[(i - 1) % len(par3_corner_points)][0]
                        new_y = 2 * curr_y / curr_abs
                        par3_corner_points_delta.append(v[new_x, new_y])
                        new_x = 2 * curr_x / curr_abs
                        par3_corner_points_delta.append(v[new_x, new_y])
                        new_y = par3_corner_points[(i + 1) % len(par3_corner_points)][1]
                        par3_corner_points_delta.append(v[new_x, new_y])
                else:
                    par3_corner_points_delta.append(par3_corner_points[i].copy())

            par3_lines_delta = [
                m.Line(
                    par3_corner_points_delta[i], 
                    par3_corner_points_delta[(i + 1) % len(par3_corner_points_delta)],
                    color = m.YELLOW
                )
                for i in range(len(par3_corner_points_delta))
            ]

            self.play(
                *(m.FadeOut(line) for line in par3_lines),
                *(m.Write(line) for line in par3_lines_delta),
                run_time=2
            )

            self.wait(0.5)

            par3_corner_points = par3_corner_points_delta
            par3_corner_points_delta = []
            par3_lines = par3_lines_delta
            par3_lines_delta = []
        
        text_par3_04 = m.Text('И так далее до бесконечности...', font='CMU Serif'
        ).scale(0.8).to_edge(m.DOWN)
        circle_par3_02 = m.Circle(2, color=m.YELLOW)

        self.play(m.Write(text_par3_04))
        self.wait(1)
        self.play(
            *(m.FadeOut(line) for line in par3_lines),
            m.FadeIn(circle_par3_02),
            run_time=3
        )
        self.wait(1)

    ### outro
        circle_par3_03 = m.Circle(0.3, color=m.RED
        ).next_to(text_par3_01, direction=m.DOWN, aligned_edge=m.LEFT)
        text_par3_05 = m.Text('=', font='CMU Serif'
        ).scale(0.8).next_to(circle_par3_03)
        circle_par3_04 = m.Circle(0.3, m.YELLOW
        ).next_to(text_par3_05)

        self.play(m.TransformFromCopy(circle_par3_01, circle_par3_03))
        self.play(m.FadeIn(text_par3_05), run_time=0.5)
        self.play(
            m.TransformFromCopy(circle_par3_02, circle_par3_04),
            m.FadeOut(text_par3_04)
        )

        self.wait(1)

        text_par3_06 = m.MathTex(r'\Longrightarrow'
        ).next_to(circle_par3_03, direction=m.DOWN, aligned_edge=m.LEFT)
        text_par3_07_a = m.MathTex(r'2\pi', color=m.RED
        ).next_to(text_par3_06)
        text_par3_08 = m.Text('=', font='CMU Serif'
        ).scale(0.8).next_to(text_par3_07_a)
        text_par3_09_a = m.Text('8', color=m.YELLOW, font='CMU Serif'
        ).scale(0.7).next_to(text_par3_08)

        self.play(m.FadeIn(text_par3_06), run_time=0.5)
        self.play(
            m.TransformFromCopy(text_par3_03_1, text_par3_07_a)
        )
        self.play(m.FadeIn(text_par3_08), run_time=0.5)
        self.play(m.TransformFromCopy(text_par3_02, text_par3_09_a))

        text_par3_07 = m.MathTex(r'\pi', color=m.RED
        ).next_to(text_par3_06, buff=0.45)
        text_par3_09 = m.Text('4', color=m.YELLOW, font='CMU Serif'
        ).scale(0.7).next_to(text_par3_08)

        self.play(
            m.ReplacementTransform(text_par3_07_a, text_par3_07),
            m.ReplacementTransform(text_par3_09_a, text_par3_09)
        )

        image_par3_01 = m.ImageMobject('images/sneaky.jpg'
        ).scale(0.55).next_to(text_par3_06, direction=m.DOWN, aligned_edge=m.LEFT)

        self.play(m.FadeIn(image_par3_01, shift=m.RIGHT), run_time=1.5)

    # End
        self.wait(4)
