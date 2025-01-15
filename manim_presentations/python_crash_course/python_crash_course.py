from manim import *
from manim_presentations.utils import *
from manim import config

SKIPA = False

PROMPT_COLOR = UT_BURNT_ORANGE
OUTPUT_COLOR = UT_DARK_GRAY

learning_goals = [
    "You will be able to setup and manage Python environments.",
    "You will understand the basics of Python code.",
    "You will be able to use Python to translate your ideas into code.",
]


class PythonCrashCourse(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Python Crash Course")
        python_logo = ImageMobject("images/python-logo").set(height=2.5)
        subtitle = Text("Just about everything you will need to start using Python in 2025.", **TEXT_BODY_STYLE)
        subtitle.to_edge(DOWN)

        self.show_title()
        self.play(FadeIn(python_logo))
        self.play(Write(subtitle))
        self.wait()


class ProgrammingInYourToolkit(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("""
        Programming:
        Part of a modern scientist's toolkit
        """)
        w = config["frame_width"] * 0.3
        omics = ImageMobject("images/omics-cube").set(width=w)
        brain = ImageMobject("images/brain-connections").set(width=w)
        eegs = ImageMobject("images/eeg-waveforms").set(width=w)
        subtitle = Text("Datasets too large/complex to handle manually", **TEXT_BODY_STYLE)

        omics.next_to(brain, LEFT)
        eegs.next_to(brain, RIGHT)
        images = Group(omics, brain, eegs)
        subtitle.to_edge(DOWN)
        images.move_to((self.title.get_center() + subtitle.get_center()) / 2)

        self.show_title()
        self.play(FadeIn(images))
        self.play(Write(subtitle))
        self.wait()


class InterpretedVsCompiled(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Interpreted vs Compiled")

        source_code = ImageMobject("images/source-code-file").set(height=2.5)
        machine_code = ImageMobject("images/machine-code-file").set(height=2.5)
        robot = ImageMobject("images/robot").set(height=2.5)
        human = ImageMobject("images/human").set(height=2.5)

        machine_code.next_to(source_code, RIGHT, buff=2.5)
        arrow = Arrow(source_code.get_center(), machine_code.get_center(), buff=1.5, color=FG_COLOR)
        human.next_to(source_code, DOWN)
        robot.next_to(machine_code, DOWN)
        group = Group(source_code, machine_code, human, robot, arrow)
        group.next_to(self.title, DOWN, buff=1)
        compile = Text("Compile", **TEXT_BODY_STYLE).next_to(arrow, UP)

        source_code_pros = Text(
            """
            Humans
            understand

            Runs
            everywhere
            """, **TEXT_BODY_STYLE).set(color=UT_DARK_BLUE)
        source_code_cons = Text(
            """
            Slower
            execution
            """, **TEXT_BODY_STYLE).set(color=RED)
        machine_code_pros = Text(
            """
            Optimized
            execution
            """, **TEXT_BODY_STYLE).set(color=UT_DARK_BLUE)
        machine_code_cons = Text(
            """
            Humans
            don't
            understand

            Runs only
            on specific
            hardware
            """, **TEXT_BODY_STYLE).set(color=RED)
        source_code_cons.next_to(source_code_pros, DOWN, buff=1, aligned_edge=LEFT)
        machine_code_pros.next_to(machine_code_cons, DOWN, buff=1, aligned_edge=LEFT)
        source_code_thumbs_up = ImageMobject("images/thumbs-up").set(height=0.5)
        source_code_thumbs_down = ImageMobject("images/thumbs-down")
        machine_code_thumbs_up = ImageMobject("images/thumbs-up")
        machine_code_thumbs_down = ImageMobject("images/thumbs-down")
        source_code_thumbs_up.set(height=0.5).next_to(source_code_pros, LEFT)
        source_code_thumbs_down.set(height=0.5).next_to(source_code_cons, LEFT)
        machine_code_thumbs_up.set(height=0.5).next_to(machine_code_pros, LEFT)
        machine_code_thumbs_down.set(height=0.5).next_to(machine_code_cons, LEFT)

        source_code_pros_cons = Group(source_code_pros, source_code_cons, source_code_thumbs_up, source_code_thumbs_down)
        machine_code_pros_cons = Group(machine_code_pros, machine_code_cons, machine_code_thumbs_up, machine_code_thumbs_down)
        source_code_pros_cons.to_edge(LEFT).align_to(source_code, UP)
        machine_code_pros_cons.to_edge(RIGHT).align_to(machine_code, UP)
        
        pros_cons = VGroup(source_code_pros, source_code_cons, machine_code_cons, machine_code_pros)
        thumbs = Group(source_code_thumbs_up, source_code_thumbs_down, machine_code_thumbs_down, machine_code_thumbs_up)

        self.show_title()
        self.play(FadeIn(group), Write(compile))
        self.wait()

        self.next_slide()
        self.play(Write(pros_cons), FadeIn(thumbs))
        self.wait()

        self.next_slide()
        title = self.title
        self.init_title("Python = Syntax + Interpreter")
        self.play(FadeOut(pros_cons), FadeOut(thumbs), Transform(title, self.title))
        self.play(Indicate(source_code))
        self.play(Indicate(arrow), Indicate(compile))
        self.wait()


class FlavorsOfPython(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Python Interpreters (Flavors)")
        flavors = ImageMobject("images/python-flavors").set(height=5)
        circle = Ellipse(width=flavors.get_width()/2, height=flavors.get_height()/4, color=UT_BURNT_ORANGE, stroke_width=4)
        in_this_course = Text("""
        In this course
        we will use
        the standard
        CPython
        interpreter.
        """, **TEXT_BODY_STYLE).set(color=UT_BURNT_ORANGE)

        flavors.next_to(self.title, DOWN, buff=1)
        circle.align_to(flavors, UL).shift(0.3*LEFT).shift(0.3*UP)
        in_this_course.next_to(flavors, LEFT, buff=0.5, aligned_edge=UP)

        self.show_title()
        self.play(FadeIn(flavors))
        self.play(Create(circle), Write(in_this_course))
        self.wait()


class AlternativesToPython(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Some Alternatives to Python")
        matlab_logo = ImageMobject("images/matlab-logo").set(height=2)
        R_logo = ImageMobject("images/R-logo").set(height=2)
        julia_logo = ImageMobject("images/julia-logo").set(height=2)
        logos = [matlab_logo, R_logo, julia_logo]
        for i in range(1, len(logos)):
            logos[i].next_to(logos[i-1], RIGHT, buff=1)
        group = Group(*logos).center()

        self.show_title()
        self.play(FadeIn(group))
        self.wait()


class LearningGoals0(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Learning Goals")
        self.init_goals(learning_goals)
        self.show_title()
        self.show_goals(0)
        self.wait()


class PythonPackageEcosystem(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Python Package Ecosystem")
        subtitle = Text("One of the primary reasons for choosing Python.", **TEXT_BODY_STYLE)
        subtitle.to_edge(DOWN)

        packages = ImageMobject("images/python-package-ecosystem").set(height=5)
        circle = Ellipse(width=2, height=1.5, color=UT_BURNT_ORANGE, stroke_width=4)
        packages.move_to((self.title.get_center() + subtitle.get_center()) / 2)
        circle.align_to(packages, DR).shift(0.2*RIGHT).shift(UP)

        self.show_title()
        self.play(GrowFromCenter(packages))
        self.play(Create(circle))
        self.play(Write(subtitle))
        self.wait()


class PackageDependencyGraph(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Package Dependency Graph")
        graph = ImageMobject("images/package-dependency-graph").set(height=5)
        versions = MarkupText(r"""
        Dependencies can also
        be <b><i>version specific</i></b>!
        """, **TEXT_BODY_STYLE)
        conflict = MarkupText(r"""
        <b><u>!! Dependency Conflict !!</u></b>
        If zlib depends on sqlite version 2.1
        and ncurses depends on sqlite version 3.0
        """, **TEXT_BODY_STYLE).set(color=RED)
        not_if_when = MarkupText(r"""
        It is not a question of <b><i>if</i></b> you
        will get a dependency conflict,
        but <b><i>when</i></b>.
        """, **TEXT_BODY_STYLE)
        zlib_dep_version = Text(r"2.1", **TEXT_BODY_STYLE).set(color=RED)
        ncurses_dep_version = Text(r"3.0", **TEXT_BODY_STYLE).set(color=RED)
        zlib_dep_version.move_to((2.15, -0.15, 0))
        ncurses_dep_version.move_to((2.3, -0.8, 0))

        graph.next_to(self.title, DOWN, buff=0.5)
        versions.to_corner(DL)
        conflict.to_corner(DL)
        not_if_when.to_corner(DL)
        
        self.show_title()
        self.play(FadeIn(graph))
        self.play(Write(versions))
        self.wait()

        self.next_slide()
        self.play(Transform(versions, conflict), Write(zlib_dep_version), Write(ncurses_dep_version))
        self.wait()

        x = VGroup(Line((-0.5, -0.5, 0), (0.5, 0.5, 0), stroke_width=9), Line((-0.5, 0.5, 0), (0.5, -0.5, 0), stroke_width=9)).set_color(RED)
        x.move_to((3.35, 0.8, 0))
        self.play(Create(x))

        self.next_slide()
        self.play(Transform(versions, not_if_when))
        self.wait()


class PackageManagers(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Package Managers")
        graph = ImageMobject("images/python-package-dependency-graph").set(height=5)
        graph_caption = Text("Python Package Dependency Graph", **TEXT_BODY_STYLE)
        not_for_humans = MarkupText(r"""
        Managing dependencies is
        <b><i>NOT for humans</i></b>!
        """, **TEXT_BODY_STYLE)
        pkg_managers = MarkupText(r"""
        Fortunately, we have 
        package managers for this...
        """, **TEXT_BODY_STYLE)
        h = 0.75
        conda_logo = ImageMobject("images/conda-logo").set(height=h)
        pip_logo = ImageMobject("images/pip-logo").set(height=h)
        mamba_logo = ImageMobject("images/mamba-logo").set(height=h)
        pdm_logo = ImageMobject("images/pdm-logo").set(height=h)
        poetry_logo = ImageMobject("images/poetry-logo").set(height=h)
        hatch_logo = ImageMobject("images/hatch-logo").set(height=h)
        logos = Group(conda_logo, mamba_logo, pdm_logo, pip_logo, poetry_logo, hatch_logo)
        and_more = Text("...and more", **TEXT_BODY_STYLE)
        in_this_course = MarkupText("""
        In this course, we will
        use <b>pip</b> and <b>conda</b>,
        but you are free to use any
        package manager you like.
        """, **TEXT_BODY_STYLE)
        
        graph_caption.scale(0.75).to_corner(DL)
        graph.next_to(graph_caption, UP).align_to(graph_caption, LEFT)
        not_for_humans.next_to(graph, RIGHT, buff=1, aligned_edge=UP)
        pkg_managers.next_to(not_for_humans, DOWN, buff=0.5, aligned_edge=LEFT)
        pip_logo.next_to(pkg_managers, DOWN, aligned_edge=LEFT)
        conda_logo.next_to(pip_logo, RIGHT)
        mamba_logo.next_to(conda_logo, RIGHT)
        pdm_logo.next_to(pip_logo, DOWN, aligned_edge=LEFT)
        poetry_logo.next_to(pdm_logo, RIGHT)
        hatch_logo.next_to(poetry_logo, RIGHT)
        and_more.next_to(pdm_logo, DOWN, aligned_edge=LEFT)
        in_this_course.align_to(pkg_managers, UL)
        
        self.show_title()
        self.play(FadeIn(graph), FadeIn(graph_caption))
        self.play(Write(not_for_humans))
        self.wait()
        
        self.next_slide()
        self.play(Write(pkg_managers))
        self.play(FadeIn(logos), Write(and_more))
        self.wait()
        
        self.next_slide()
        pip_conda_group = Group(pip_logo, conda_logo)
        self.play(Transform(pkg_managers, in_this_course), FadeOut(Group(mamba_logo, pdm_logo, poetry_logo, hatch_logo, and_more)), pip_conda_group.animate.scale(1.4, about_point=pip_conda_group.get_corner(UL)).next_to(in_this_course, DOWN, buff=0.5, aligned_edge=LEFT))
        self.wait()


class InstallConda(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Install Conda")

        msg = MarkupText("I recommend installing <b>miniforge</b> which includes conda.", **TEXT_BODY_STYLE)
        msg.chars[20:29].set_color(UT_BURNT_ORANGE)

        msg2 = Text("""
                    Install as directed at https://github.com/conda-forge/miniforge.
                    """, **TEXT_BODY_STYLE)
        msg2.chars[19:-1].set_color(UT_ADOBE_BLUE)

        msg3 = Text("""
                    Then use conda in a command shell or terminal.
                    """, **TEXT_BODY_STYLE)

        msg4 = Text("""
                    Yeah, I know. Learn to love your shell.
                    """, **TEXT_BODY_STYLE)
        msg4.chars[11:].set_color(UT_BURNT_ORANGE)

        msgs = VGroup(msg, msg2, msg3, msg4).arrange(DOWN, buff=0.75)

        self.show_title()
        self.play(Write(msg))
        self.play(Write(msg2, run_time=0.75))
        self.play(Write(msg3, run_time=0.75))
        self.play(Write(msg4))
        self.wait()


class CondaHelp(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Conda")
        self.show_title()

        shell = self.create_code_cell(position='LEFT', code=">", **SHELL_STYLE)
        shell.code.set_color(PROMPT_COLOR)
        self.add(shell)

        msg = Text("""
                   You will use conda within a shell
                   (e.g., cmd shell or Terminal).
                   """, **TEXT_BODY_STYLE)
        msg.next_to(shell, RIGHT)
        self.play(Write(msg))
        self.wait()

        # conda --help
        self.next_slide()
        shell.append_code(" conda --help", player=self)
        shell.append_code("""
This will print out a bunch of
instructions on how to use conda...""", player=self, color=OUTPUT_COLOR)
        shell.append_code("\n>", player=self, color=PROMPT_COLOR)
        self.wait()


class VirtualEnvironments0(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Virtual Environments")
        self.show_title()

        venv_folder = ImageMobject("images/folder")
        venv_folder.set(width=5)
        venv_folder.to_edge(LEFT)

        msg = Text("""
                   A virtual environment is essentially
                   just a folder on your computer
                   where you will store a particular
                   collection of python packages.""", **TEXT_BODY_STYLE)
        msg.next_to(venv_folder, RIGHT)
        
        self.play(FadeIn(venv_folder), FadeIn(msg))

        logos = Group(
            ImageMobject("images/python-logo").set(width=1),
            ImageMobject("images/numpy-logo").set(width=1),
            ImageMobject("images/scipy-logo").set(width=1)
        )
        logos.arrange(RIGHT, buff=MARGIN).move_to(venv_folder)
        self.play(FadeIn(logos, shift=8*DOWN, lag_ratio=0.3))
        self.wait()

        self.next_slide()
        subtitle = Text("You can have as many virtual environments as you want.", **TEXT_BODY_STYLE)
        subtitle.to_edge(DOWN)

        venv_folders = Group(*[ImageMobject("images/folder").set(width=venv_folder.width) for i in range(2)]).arrange(RIGHT, buff=0.5).next_to(venv_folder, RIGHT, buff=0.5)

        self.play(Write(subtitle), FadeOut(msg), FadeIn(venv_folders))
        self.wait()

        self.next_slide()
        old_subtitle = subtitle
        subtitle = Text("Each one can have a different collection of packages.", **TEXT_BODY_STYLE).to_edge(DOWN)
        logos2 = Group(
            ImageMobject("images/python-logo").set(width=1),
            ImageMobject("images/numpy-logo").set(width=1),
            ImageMobject("images/jupyter-logo").set(width=1)
        )
        logos2.arrange(RIGHT, buff=MARGIN).move_to(venv_folders[0])
        
        self.play(Transform(old_subtitle, subtitle, replace_mobject_with_target_in_scene=True), FadeIn(logos2, shift=8*DOWN, lag_ratio=0.3))
        self.wait()

        self.next_slide()
        old_subtitle = subtitle
        subtitle = Text("Or different versions of the same package.", **TEXT_BODY_STYLE).to_edge(DOWN)

        version_style = TEXT_BODY_STYLE.copy()
        version_style["font"] = "Monospace"
        version_style["font_size"] = 24
        package_versions = VGroup(Text("2.0", **version_style), Text("1.20", **version_style))
        package_versions[0].next_to(logos[1], DOWN)
        package_versions[1].next_to(logos2[1], DOWN)
        
        self.play(Transform(old_subtitle, subtitle, replace_mobject_with_target_in_scene=True), Write(package_versions))
        self.wait()

        self.next_slide()
        old_subtitle = subtitle
        subtitle = Text("Conda can even manage different versions of Python.", **TEXT_BODY_STYLE).to_edge(DOWN)

        python_versions = VGroup(Text("3.12", **version_style), Text("2.10", **version_style))
        python_versions[0].next_to(logos[0], DOWN).align_to(package_versions[0], DOWN)
        python_versions[1].next_to(logos2[0], DOWN).align_to(package_versions[1], DOWN)
        
        self.play(Transform(old_subtitle, subtitle, replace_mobject_with_target_in_scene=True), Write(python_versions))
        self.wait()

        self.next_slide()
        old_subtitle = subtitle
        subtitle = Text("""
                        I strongly suggest that you create
                        a new environment for each project.
                        """, **TEXT_BODY_STYLE).to_edge(DOWN)
        self.play(Transform(old_subtitle, subtitle, replace_mobject_with_target_in_scene=True))
        self.wait()

        self.next_slide()
        msg = Text("""
                   This way when you have a problem
                   you can wipe and restore the
                   environment without affecting
                   your other projects.""", **TEXT_BODY_STYLE)
        msg.next_to(venv_folder, RIGHT)
        self.play(FadeOut(venv_folders), FadeOut(logos2), FadeOut(package_versions[1]), FadeOut(python_versions[1]), FadeIn(msg))

        self.next_slide()
        pyfile = ImageMobject("images/file").set(height=2)
        pyfile.next_to(venv_folder, RIGHT)
        script = VGroup(
            Tex(".py", **TEX_BODY_STYLE).set_color(WHITE),
            Tex("script", **TEX_BODY_STYLE).set_color(WHITE)
        ).arrange(DOWN, buff=0.3).move_to(pyfile)
        msgs = VGroup(MarkupText("""
                         Python scripts you write are
                         <b>NOT</b> part of any environment.
                         """, **TEXT_BODY_STYLE), MarkupText("""
                         Environments only contain
                         the packages your scripts
                         depend on.
                         """, **TEXT_BODY_STYLE), MarkupText("""
                         <i>You select an environment to
                         use when you run your scripts.</i>
                         """, **TEXT_BODY_STYLE).set_color(UT_BURNT_ORANGE))
        msgs.arrange(DOWN, buff=0.6, aligned_edge=LEFT).next_to(pyfile, RIGHT)
        
        self.play(FadeOut(subtitle), FadeOut(msg), FadeIn(pyfile), FadeIn(script), Write(msgs[0]))
        self.play(Write(msgs[1:]))
        self.wait()


class VirtualEnvironments1(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Virtual Environments")
        self.add(self.title)

        shell = self.create_code_cell(position='LEFT', code="(base)>", **SHELL_STYLE)
        shell.code.set_color(PROMPT_COLOR)
        self.add(shell)

        base_folder = ImageMobject("images/folder")
        base_folder.set(width=shell.width)
        base_folder.next_to(shell, RIGHT, buff=MARGIN)
        label_style = TEXT_BODY_STYLE.copy()
        label_style["font_size"] = 28
        base_label = Text("base", **label_style)
        base_label.align_to(base_folder, UL).shift((0.5, -0.2, 0))
        base_dir = Group(base_folder, base_label)
        self.play(FadeIn(base_dir, shift=5*DOWN))
        self.wait()

        # conda env list
        self.next_slide()
        shell.append_code(" conda env list", player=self)
        shell.append_code("""
# conda environments:
#
base     *  .../base""", player=self, color=OUTPUT_COLOR)
        shell.append_code("\n(base)>", player=self, color=PROMPT_COLOR)
        self.wait()

        # conda create --name neu365p
        self.next_slide()
        shell.append_code(" create --name neu365p", player=self)
        shell.append_code("\n(base)>", player=self, color=PROMPT_COLOR)

        base_dir.align_to(shell, UP)

        neu_folder = ImageMobject("images/folder")
        neu_folder.set(width=base_folder.width)
        neu_folder.move_to(base_folder)
        neu_label = Text("neu365p", **label_style)
        neu_label.align_to(base_label, UL)
        neu_dir = Group(neu_folder, neu_label)
        neu_dir.next_to(base_dir, DOWN, buff=MARGIN)
        neu_label.set_opacity(0.5)
        self.play(FadeIn(neu_dir, shift=5*UP))
        self.wait()

        # conda env list
        self.next_slide()
        shell.append_code(" conda env list", player=self)
        shell.append_code("""
# conda environments:
#
base     *  .../base
neu365p     .../neu365p""", player=self, color=OUTPUT_COLOR)
        shell.append_code("\n(base)>", player=self, color=PROMPT_COLOR)
        self.wait()

        # conda activate neu365p
        self.next_slide()
        shell.append_code(" conda activate neu365p", player=self)
        shell.append_code("\n(neu365p)>", player=self, color=PROMPT_COLOR)

        self.play(neu_dir.animate.align_to(shell, UP), base_dir.animate.align_to(neu_dir, UP))
        neu_label.set_opacity(1)
        base_label.set_opacity(0.5)
        self.wait()

        # conda env list
        self.next_slide()
        shell.scroll_to_last_line(player=self)
        shell.append_code(" conda env list", player=self)
        shell.append_code("""
# conda environments:
#
base        .../base
neu365p  *  .../neu365p""", player=self, color=OUTPUT_COLOR)
        shell.append_code("\n(neu365p)>", player=self, color=PROMPT_COLOR)
        self.wait()


class VirtualEnvironments2(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Virtual Environments")
        self.add(self.title)

        shell = self.create_code_cell(position='LEFT', code="(neu365p)>", **SHELL_STYLE)
        shell.code.set_color(PROMPT_COLOR)
        self.add(shell)

        base_folder = ImageMobject("images/folder")
        base_folder.set(width=shell.width)
        base_folder.next_to(shell, RIGHT, buff=MARGIN)
        label_style = TEXT_BODY_STYLE.copy()
        label_style["font_size"] = 28
        base_label = Text("base", **label_style)
        base_label.align_to(base_folder, UL).shift((0.5, -0.2, 0))
        base_label.set_opacity(0.5)
        base_dir = Group(base_folder, base_label)

        neu_folder = ImageMobject("images/folder")
        neu_folder.set(width=base_folder.width)
        neu_folder.move_to(base_folder)
        neu_label = Text("neu365p", **label_style)
        neu_label.align_to(base_label, UL)
        neu_dir = Group(neu_folder, neu_label)

        neu_dir.align_to(shell, UP)
        base_dir.next_to(neu_dir, DOWN, buff=MARGIN)
        self.add(base_dir, neu_dir)
        self.wait()

        # conda install python
        self.next_slide()
        shell.append_code(" conda install python", player=self)
        shell.append_code("\n(neu365p)>", player=self, color=PROMPT_COLOR)
        
        dir_style = TEXT_BODY_STYLE.copy()
        dir_style["font_size"] = 24
        dir_style["font"] = "Monospace"
        dir_style["line_spacing"] = 0.7
        neu_packages = Text("""
                            pip     24.3.1
                            python  3.12.7
                            ...
                            """, **dir_style)
        neu_packages.next_to(neu_label, DOWN, buff=0.6, aligned_edge=LEFT)
        self.play(Write(neu_packages))
        self.wait()

        # conda list
        self.next_slide()
        shell.append_code(" conda list", player=self)
        shell.append_code("""
# packages in environment at neu365p:
#
# Name      Version
pip         24.3.1
python      3.12.7
...""", player=self, color=OUTPUT_COLOR)
        shell.append_code("\n(neu365p)>", player=self, color=PROMPT_COLOR)
        self.wait()

        # conda install python=3.10
        self.next_slide()
        shell.append_code("=3.10", line_index=0, player=self)
        shell.remove_code((-3, -6), (-3, None))
        shell.append_code("3.10.16", line_index=-3, player=self, color=OUTPUT_COLOR)

        tmp_packages = Text("""
                            pip     24.3.1
                            python  3.10.16
                            ...
                            """, **dir_style)
        tmp_packages.align_to(neu_packages, UL)
        self.remove(neu_packages)
        del neu_packages
        neu_packages = tmp_packages
        self.add(neu_packages)

        self.store_mobjects()
        self.play(Indicate(shell.code[0][-5:], color=YELLOW, run_time=2), Indicate(shell.code[-3][-7:], color=YELLOW, run_time=2), Indicate(neu_packages.chars[-10:-3], color=YELLOW, run_time=2))
        self.restore_mobjects()
        self.wait()

        # conda install "python<3.12"
        self.next_slide()
        shell.remove_code((0, -11), (0, None))
        shell.append_code("\"python<3.12\"", line_index=0, player=self)
        shell.remove_code((-3, -7), (-3, None))
        shell.append_code("3.11.9", line_index=-3, player=self, color=OUTPUT_COLOR)

        tmp_packages = Text("""
                            pip     24.3.1
                            python  3.11.9
                            ...
                            """, **dir_style)
        tmp_packages.align_to(neu_packages, UL)
        self.remove(neu_packages)
        del neu_packages
        neu_packages = tmp_packages
        self.add(neu_packages)

        self.store_mobjects()
        self.play(Indicate(shell.code[0][-13:], color=YELLOW, run_time=2), Indicate(shell.code[-3][-6:], color=YELLOW, run_time=2), Indicate(neu_packages.chars[-9:-3], color=YELLOW, run_time=2))
        self.restore_mobjects()
        self.wait()


class VirtualEnvironments3(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Virtual Environments")
        self.add(self.title)

        shell = self.create_code_cell(position='LEFT', code="(neu365p)>", **SHELL_STYLE)
        shell.code.set_color(PROMPT_COLOR)
        self.add(shell)

        base_folder = ImageMobject("images/folder")
        base_folder.set(width=shell.width)
        base_folder.next_to(shell, RIGHT, buff=MARGIN)
        label_style = TEXT_BODY_STYLE.copy()
        label_style["font_size"] = 28
        base_label = Text("base", **label_style)
        base_label.align_to(base_folder, UL).shift((0.5, -0.2, 0))
        base_label.set_opacity(0.5)
        base_dir = Group(base_folder, base_label)

        neu_folder = ImageMobject("images/folder")
        neu_folder.set(width=base_folder.width)
        neu_folder.move_to(base_folder)
        neu_label = Text("neu365p", **label_style)
        neu_label.align_to(base_label, UL)
        neu_dir = Group(neu_folder, neu_label)

        neu_dir.align_to(shell, UP)
        base_dir.next_to(neu_dir, DOWN, buff=MARGIN)

        dir_style = TEXT_BODY_STYLE.copy()
        dir_style["font_size"] = 24
        dir_style["font"] = "Monospace"
        dir_style["line_spacing"] = 0.7
        neu_packages = Text("""
                            pip     24.3.1
                            python  3.11.9
                            ...
                            """, **dir_style)
        neu_packages.next_to(neu_label, DOWN, buff=0.6, aligned_edge=LEFT)

        self.add(base_dir, neu_dir, neu_packages)
        self.wait()

        # pip install ipykernel
        self.next_slide()
        shell.append_code(" pip install ipykernel", player=self)
        shell.append_code("\n(neu365p)>", player=self, color=PROMPT_COLOR)

        tmp_packages = Text("""
                            ipykernel  6.29.5
                            pip        24.3.1
                            python     3.11.9
                            ...""", **dir_style)
        tmp_packages.align_to(neu_packages, UL)
        self.remove(neu_packages)
        del neu_packages
        neu_packages = tmp_packages
        self.add(neu_packages)
        self.wait()

        # pip list
        self.next_slide()
        shell.append_code(" pip list", player=self)
        shell.append_code("""
Package     Version
----------- -----------
ipykernel   6.29.5
...""", player=self, color=OUTPUT_COLOR)
        shell.append_code("\n(neu365p)>", player=self, color=PROMPT_COLOR)
        self.wait()

        # pip install ipykernel==6.10.0
        self.next_slide()
        shell.append_code("==6.10.0", line_index=0, player=self)
        shell.remove_code((-3, -6), (-3, None))
        shell.append_code("6.10.0", line_index=-3, player=self, color=OUTPUT_COLOR)

        tmp_packages = Text("""
                            ipykernel  6.10.0
                            pip        24.3.1
                            python     3.11.9
                            ...""", **dir_style)
        tmp_packages.align_to(neu_packages, UL)
        self.remove(neu_packages)
        del neu_packages
        neu_packages = tmp_packages
        self.add(neu_packages)

        self.store_mobjects()
        self.play(Indicate(shell.code[0][-8:], color=YELLOW, run_time=2), Indicate(shell.code[-3][-6:], color=YELLOW, run_time=2), Indicate(neu_packages.chars[9:15], color=YELLOW, run_time=2))
        self.restore_mobjects()
        self.wait()

        # pip install "ipykernel<=6.3"
        self.next_slide()
        shell.remove_code((0, -17), (0, None))
        shell.append_code("\"ipykernel<=6.3\"", line_index=0, player=self)
        shell.remove_code((-3, -6), (-3, None))
        shell.append_code("6.3.0", line_index=-3, player=self, color=OUTPUT_COLOR)

        tmp_packages = Text("""
                            ipykernel  6.3.0
                            pip        24.3.1
                            python     3.11.9
                            ...""", **dir_style)
        tmp_packages.align_to(neu_packages, UL)
        self.remove(neu_packages)
        del neu_packages
        neu_packages = tmp_packages
        self.add(neu_packages)

        self.store_mobjects()
        self.play(Indicate(shell.code[0][-16:], color=YELLOW, run_time=2), Indicate(shell.code[-3][-5:], color=YELLOW, run_time=2), Indicate(neu_packages.chars[9:14], color=YELLOW, run_time=2))
        self.restore_mobjects()
        self.wait()

        # conda list
        self.next_slide()
        shell.append_code(" conda list", player=self)
        shell.append_code("""
# packages in environment at neu365p:
#
# Name      Version
ipykernel   6.3.0
pip         24.3.1
python      3.11.9
...""", player=self, color=OUTPUT_COLOR)
        shell.append_code("\n(neu365p)>", player=self, color=PROMPT_COLOR)
        self.wait()


class VirtualEnvironments4(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Virtual Environments")
        self.add(self.title)

        shell = self.create_code_cell(position='LEFT', code="(neu365p)>", **SHELL_STYLE)
        shell.code.set_color(PROMPT_COLOR)
        self.add(shell)

        base_folder = ImageMobject("images/folder")
        base_folder.set(width=shell.width)
        base_folder.next_to(shell, RIGHT, buff=MARGIN)
        label_style = TEXT_BODY_STYLE.copy()
        label_style["font_size"] = 28
        base_label = Text("base", **label_style)
        base_label.align_to(base_folder, UL).shift((0.5, -0.2, 0))
        base_label.set_opacity(0.5)
        base_dir = Group(base_folder, base_label)

        neu_folder = ImageMobject("images/folder")
        neu_folder.set(width=base_folder.width)
        neu_folder.move_to(base_folder)
        neu_label = Text("neu365p", **label_style)
        neu_label.align_to(base_label, UL)

        dir_style = TEXT_BODY_STYLE.copy()
        dir_style["font_size"] = 24
        dir_style["font"] = "Monospace"
        dir_style["line_spacing"] = 0.7
        neu_packages = Text("""
                            ipykernel  6.3.0
                            pip        24.3.1
                            python     3.11.9
                            ...
                            """, **dir_style)
        neu_packages.next_to(neu_label, DOWN, buff=0.6, aligned_edge=LEFT)
        neu_dir = Group(neu_folder, neu_label, neu_packages)

        neu_dir.align_to(shell, UP)
        base_dir.next_to(neu_dir, DOWN, buff=MARGIN)
        self.add(base_dir, neu_dir)
        self.wait()

        # conda activate base
        self.next_slide()
        shell.append_code(" conda activate base", player=self)
        shell.append_code("\n(base)>", player=self, color=PROMPT_COLOR)

        self.play(base_dir.animate.align_to(shell, UP), neu_dir.animate.align_to(base_dir, UP))
        base_label.set_opacity(1)
        neu_label.set_opacity(0.5)
        neu_packages.set_opacity(0.5)
        self.wait()

        # conda env list
        self.next_slide()
        shell.append_code(" conda env list", player=self)
        shell.append_code("""
# conda environments:
#
base     *  .../base
neu365p     .../neu365p""", player=self, color=OUTPUT_COLOR)
        shell.append_code("\n(base)>", player=self, color=PROMPT_COLOR)
        self.wait()

        # conda env remove --name neu365P
        self.next_slide()
        shell.append_code(" conda env remove --name neu365p", player=self)
        shell.append_code("\n(base)>", player=self, color=PROMPT_COLOR)

        self.play(FadeOut(neu_dir, shift=5*DOWN))
        self.wait()

        # conda env list
        self.next_slide()
        shell.append_code(" conda env list", player=self)
        shell.append_code("""
# conda environments:
#
base     *  .../base""", player=self, color=OUTPUT_COLOR)
        shell.append_code("\n(base)>", player=self, color=PROMPT_COLOR)
        self.wait()


class PythonFiles(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Python Files")
        self.show_title()

        label_style = TEX_BODY_STYLE.copy()
        label_style["font_size"] = 64

        py_doc = ImageMobject("images/file").set(width=3)
        py_ext = Tex(".py", **label_style).move_to(py_doc).set_color(WHITE)
        py_file = Group(py_doc, py_ext)

        ipynb_doc = ImageMobject("images/file").set(width=3)
        ipynb_ext = Tex(".ipynb", **label_style).move_to(ipynb_doc).set_color(WHITE)
        ipynb_file = Group(ipynb_doc, ipynb_ext)

        Group(py_file, ipynb_file).arrange(RIGHT, buff=2)
        self.add(py_file, ipynb_file)

        py_desc = Text("""
                       Python
                       text file
                       """, **TEXT_BODY_STYLE).set_color(UT_BURNT_ORANGE)
        ipynb_desc = Text("""
                          IPython
                          Jupyter
                          notebook
                          """, **TEXT_BODY_STYLE).set_color(UT_BURNT_ORANGE)
        py_desc.next_to(py_file, LEFT, buff=0.5)
        ipynb_desc.next_to(ipynb_file, RIGHT, buff=0.5)
        self.play(Write(py_desc), Write(ipynb_desc))

        self.wait()


class RunningPythonCode(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Running Python Code")
        self.show_title()

        shell = self.create_code_cell(position='LEFT', code="(base)>", **SHELL_STYLE)
        shell.code.set_color(PROMPT_COLOR)
        self.add(shell)
        self.wait()

        # conda activate neu365p
        self.next_slide()
        msg = Text("""
                   Remember to activate your
                   desired environment before
                   running your script.
                   """, **TEXT_BODY_STYLE)
        msg.next_to(shell, RIGHT, buff=1)
        self.play(Write(msg))
        shell.append_code(" conda activate neu365p", player=self)
        shell.append_code("\n(neu365p)>", player=self, color=PROMPT_COLOR)
        self.wait()

        # go to file dir
        self.next_slide()
        old_msg = msg
        msg = Text("""
                   Navigate to the folder
                   containing your .py file.
                   """, **TEXT_BODY_STYLE)
        file_img = ImageMobject("images/file").set(height=4)
        file_label = Text("script.py", **TEX_BODY_STYLE).set_color(WHITE).move_to(file_img)
        pyfile = Group(file_img, file_label).next_to(msg, DOWN)
        Group(msg, pyfile).next_to(shell, RIGHT, buff=1)
        self.play(FadeOut(old_msg), FadeIn(msg), FadeIn(pyfile))
        shell.append_code(" cd path/to/script/folder", player=self)
        shell.append_code("\n(neu365p)>", player=self, color=PROMPT_COLOR)
        self.wait()

        # go to file dir
        self.next_slide()
        old_msg = msg
        msg = Text("""
                   Run the code in script.py 
                   using the current environment.
                   """, **TEXT_BODY_STYLE)
        msg.move_to(old_msg)
        self.play(Transform(old_msg, msg, replace_mobject_with_target_in_scene=True))
        shell.append_code(" python script.py", player=self)
        shell.append_code("\n(neu365p)>", player=self, color=PROMPT_COLOR)
        self.wait()
        

class IntegratedDevelopmentEnvironments(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Integrated Development Environments (IDEs)")
        self.show_title()

        msg = Text("""
                   Although you can do all your python code development
                   with a simple text editor and a shell,
                   you may find it more convenient to use an IDE.
                   """, **TEXT_BODY_STYLE)
        self.play(Write(msg))
        self.wait()

        self.next_slide()
        logos = Group(
            ImageMobject("images/vscode-logo").set(height=2),
            ImageMobject("images/pycharm-logo").set(height=2),
            ImageMobject("images/spyder-logo").set(height=2),
            ImageMobject("images/jupyter-logo").set(height=2)
        ).arrange(RIGHT, buff=1)
        names = VGroup(
            Text("VSCode", **TEXT_BODY_STYLE),
            Text("PyCharm", **TEXT_BODY_STYLE),
            Text("Spyder", **TEXT_BODY_STYLE),
            Text("JupyterLab", **TEXT_BODY_STYLE)
        )
        for i in range(4):
            names[i].next_to(logos[i], UP)
        self.play(msg.animate.to_edge(DOWN), FadeIn(logos, shift=5*DOWN, lag_ratio=0.25))
        self.play(FadeIn(names))
        self.wait()

        self.next_slide()
        old_msg = msg
        msg = Text("""
                   It probably does NOT matter which IDE you use
                   so long as it supports Jupyter notebooks.
                   Any of the above should give you a comparable experience.
                   """, **TEXT_BODY_STYLE)
        msg.to_edge(DOWN)
        self.play(Transform(old_msg, msg, replace_mobject_with_target_in_scene=True))
        self.wait()

        self.next_slide()
        vscode_screenshot = ImageMobject("images/vscode-screenshot").set(height=6)
        vscode_screenshot.next_to(self.title, DOWN)
        vscode_logo = Group(logos[0], names[0])
        logos.remove(logos[0])
        names.remove(names[0])
        self.play(FadeOut(logos), FadeOut(names), FadeOut(msg), vscode_logo.animate.to_edge(LEFT), FadeIn(vscode_screenshot))
        self.wait()

        self.next_slide()
        python_ext_screenshot = ImageMobject("images/vscode-python-extension").set(height=vscode_screenshot.height).move_to(vscode_screenshot)
        subtitle = Text("For VSCode, you will need the Python and Jupyter extensions.", **TEXT_BODY_STYLE).to_edge(DOWN)
        self.play(FadeOut(vscode_screenshot), FadeIn(python_ext_screenshot), Write(subtitle))
        circle = Circle(radius=0.2, color=RED, stroke_width=7).set_z_index(2).move_to((-3.86, 0.75, 0))
        self.play(Create(circle))
        self.wait()

        self.next_slide()
        jupyter_ext_screenshot = ImageMobject("images/vscode-jupyter-extension").set(height=python_ext_screenshot.height).move_to(python_ext_screenshot)
        self.play(FadeOut(python_ext_screenshot), FadeIn(jupyter_ext_screenshot))
        self.wait()


class LearningGoals1(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Learning Goals")
        self.init_goals(learning_goals)
        self.show_title()
        self.show_goals(1)
        self.wait()


class BasicDataTypes(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Basic Data Types")
        types = ["bool", "int", "float", "str", "None"]
        examples = ["True, False", "-1, 0, 100", "-3.14, 0.0, 8e2", "\"Hello world!\", 'Neuro rocks', \"Hi y'all.\"", "None"]
        types = [Text(type, **TEXT_BODY_STYLE).set(color=UT_BURNT_ORANGE) for type in types]
        self.add(*types)
        examples = [Code(code=example, **CODE_STYLE) for example in examples]

        VGroup(*types).arrange(DOWN, buff=0.75, aligned_edge=RIGHT)
        for i in range(len(examples)):
            examples[i].next_to(types[i], RIGHT, buff=0.75)
        VGroup(*types, *examples).next_to(self.title, DOWN, buff=0.5)
        
        self.show_title()
        self.play(*[Write(type) for type in types], *[FadeIn(example) for example in examples])
        self.wait()


class BasicOperations(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Basic Operations")
        ops = ["add", "subtract", "multiply", "divide", "power", "modulus", "floor division"]
        inputs = ["3 + 2", "3 - 2", "3 * 2", "3 / 2", "3 ** 2", "5 % 3", "5 // 3"]
        outputs = [r"$\rightarrow 5$", r"$\rightarrow 1$", r"$\rightarrow 6$", r"$\rightarrow 1.5$", r"$\rightarrow 9$", r"$\rightarrow 2$", r"$\rightarrow 1$"]
        ops = [Text(op, **TEXT_BODY_STYLE).set(color=UT_BURNT_ORANGE) for op in ops]
        inputs = [Code(code=input, **CODE_STYLE) for input in inputs]
        outputs = [Tex(output, **TEX_BODY_STYLE) for output in outputs]
        
        for i in range(1, len(inputs)):
            inputs[i].next_to(inputs[i-1], DOWN, aligned_edge=LEFT)
        for i in range(len(ops)):
            ops[i].next_to(inputs[i], LEFT)
            outputs[i].next_to(inputs[i], RIGHT)
        lgroup = VGroup(*ops[:-2], *inputs[:-2], *outputs[:-2])
        rgroup = VGroup(*ops[-2:], *inputs[-2:], *outputs[-2:])
        rgroup.next_to(lgroup, RIGHT, buff=1, aligned_edge=UP)
        group = VGroup(lgroup, rgroup)
        group.next_to(self.title, DOWN, buff=0.5)
        
        self.show_title()
        self.play(*[Write(op) for op in ops], *[FadeIn(input) for input in inputs], *[FadeIn(output) for output in outputs])
        self.wait()


class TypeAwareOperations(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Type Aware Operations")
        self.show_title()
        self.wait()


class LogicalComparisons(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Logical Comparisons")
        self.show_title()
        self.wait()


class Variables(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Variables")
        self.show_title()
        self.wait()


class NamingThings(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Naming Things")
        goldilocks = ImageMobject("images/goldilocks").set(height=3)
        self.show_title()
        self.add(goldilocks)
        self.wait()


class SpecialNamingPatterns(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Special Naming Patterns")
        self.show_title()
        self.wait()


class ShorthandOperations(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Shorthand Operations")
        self.show_title()
        self.wait()


class Output(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Output")
        self.show_title()
        self.wait()


class Whitespace(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Whitespace")
        self.show_title()
        self.wait()


class Comments(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Comments")
        self.show_title()
        self.wait()


class MultiLineStrings(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Multi-Line Strings")
        self.show_title()
        self.wait()


class FormatStrings(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Format Strings")
        self.show_title()
        self.wait()


class UnderstandableCode(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Understandable Code")
        huh = ImageMobject("images/what-was-i-doing").set(height=6)
        self.show_title()
        huh.next_to(self.title, DOWN, buff=0.5)
        self.add(huh)
        self.wait()


class ConditionalCodeBlocks(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Conditional Code Blocks")
        self.show_title()
        self.wait()


class NestedCodeBlocks(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Nested Code Blocks")
        self.show_title()
        self.wait()


class Lists(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Lists")
        self.show_title()
        self.wait()


class ListUnpacking(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("List Unpacking")
        self.show_title()
        self.wait()


class ListIndexing(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("List Indexing")
        self.show_title()
        self.wait()


class ListSlicing(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("List Slicing")
        self.show_title()
        self.wait()


class ListSliceDefaults(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("List Slice Defaults")
        self.show_title()
        self.wait()


class MutatingLists(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Mutating Lists")
        self.show_title()
        self.wait()


class NestedLists(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Nested Lists")
        self.show_title()
        self.wait()


class Dictionaries(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Dictionaries")
        self.show_title()
        self.wait()


class MutatingDictionaries(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Mutating Dictionaries")
        self.show_title()
        self.wait()


class AssignmentVsMutation(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Assignment vs Mutation")
        self.show_title()
        self.wait()


class IteratingCollections(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Iterating Collections")
        self.show_title()
        self.wait()


class IterateUntilCondition(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Iterate Until Condition")
        self.show_title()
        self.wait()


class StoppingAndSkipping(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Stopping and Skipping")
        self.show_title()
        self.wait()


class ListComprehensions(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("List Comprehensions")
        self.show_title()
        self.wait()


class DictionaryComprehensions(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Dictionary Comprehensions")
        self.show_title()
        self.wait()


class Generators(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Generators")
        self.show_title()
        self.wait()


class Functions(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Functions")
        self.show_title()
        self.wait()


class FunctionOutput(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Function Output")
        self.show_title()
        self.wait()


class DefaultFunctionArguments(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Default Function Arguments")
        self.show_title()
        self.wait()


class NamedFunctionArguments(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Named Function Arguments")
        self.show_title()
        self.wait()


class ArgsAndKwargs(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("args and kwargs")
        self.show_title()
        self.wait()


class VariableScope(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Variable Scope")
        self.show_title()
        self.wait()


class Classes(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Classes")
        self.show_title()
        self.wait()


class ClassTemplateVsInstance(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Class Template vs Instance")
        self.show_title()
        self.wait()


class ClassTemplateAttributes(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Class Template Attributes")
        self.show_title()
        self.wait()


class ClassInstanceSpecificAttributes(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Class Instance-Specific Attributes")
        self.show_title()
        self.wait()


class ClassMethods(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Class Methods")
        self.show_title()
        self.wait()


class ClassInheritance(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Class Inheritance")
        self.show_title()
        self.wait()


class OnlyUseClassesWhenNecessary(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("!! Only Use Classes When Necessary")
        self.show_title()
        self.wait()


class Modules(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Modules")
        self.show_title()
        self.wait()


class NestedModules(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Nested Modules")
        self.show_title()
        self.wait()


class Packages(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Packages")
        self.show_title()
        self.wait()


class PythonCrashCourseLearningGoals2(DefaultSlide):
    def construct(self):
        super().construct()
        self.init_title("Learning Goals")
        self.init_goals(learning_goals)
        self.show_title()
        self.show_goals(2)
        self.wait()


if __name__ == "__main__":
    import os, ast

    startdir = os.getcwd()
    filedir, filename = os.path.split(os.path.abspath(__file__))
    os.chdir(filedir)
    
    with open(filename, 'r') as file:
        content = file.read()
    parsed = ast.parse(content)
    slides = []
    slides_to_render = []
    render = False
    for node in ast.walk(parsed):
        if isinstance(node, ast.Expr) and hasattr(node.value, "value") and node.value.value == "r":
            render = True
        if isinstance(node, ast.ClassDef) and node.name not in ["DefaultSlide"]:
            for base in node.bases:
                if isinstance(base, ast.Name) and base.id in ["DefaultSlide", "Slide"]:
                    slides.append(node.name)
                    if render:
                        slides_to_render.append(node.name)
                    break
            render = False

    # slides_to_render = []
    # slides_to_render = slides[:10]
    # slides_to_render = [slide for slide in slides if "LearningGoals" in slide]
    # slides_to_render = ["VirtualEnvironments"]
    for scene in slides_to_render:
        cmd = f"manim -p --quality=l {filename} {scene}"
        os.system(cmd)
    
    # import shutil
    # from_path = os.path.join(utils_path, "slides", "files", "CourseSplash")
    # to_path = os.path.join(filedir, "slides", "files", "CourseSplash")
    # if os.path.exists(to_path):
    #     shutil.rmtree(to_path)
    # shutil.copytree(from_path, to_path)
    # shutil.copy(os.path.join(utils_path, "slides", "CourseSplash.json"), os.path.join(filedir, "slides"))
    # slides = ["CourseSplash"] + slides
    
    # slides = slides_to_render
    # start = slides.index(slides_to_render[0]) if slides_to_render else 0
    # # start = slides.index("PythonCrashCourseLearningGoals1"])
    # # start = 4
    # cmd = f"manim-slides --sa {start},{start} {' '.join(slides)}"
    # os.system(cmd)

    os.chdir(startdir)

