from manim import *
from manim_slides import Slide
from manim_presentations.utils.config import *
from manim_presentations.utils.DynamicCode import DynamicCode

class DefaultSlide(Slide):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def construct(self):
        self.background = ImageMobject("../utils/images/backgrounds/UT-light-blue-2023-bg-only")
        self.background.set(z_index=-99)
        self.background.set(height=config['frame_height'])
        if self.background.width < config['frame_width']:
            self.background.set(width=config['frame_width'])
        self.add(self.background)
    
    def init_title(self, title):
        self.title = Text(title, **TEXT_TITLE_STYLE).to_edge(UP, buff=MARGIN)
        self.center_excluding_title = (0, -self.title.height / 2, 0)
    
    def show_title(self):
        self.play(FadeIn(self.title, lag_ratio=0.1, shift=DOWN))
    
    def init_goals(self, goals):
        self.goals_logo = ImageMobject("../utils/images/brain-machine-interface-logo").set(height=1).to_corner(UL, buff=MARGIN)
        self.goals = BulletedList(*goals, **TEX_BODY_STYLE).set_color(FG_COLOR)
    
    def show_goals(self, selected=None):
        self.play(Write(self.goals), FadeIn(self.goals_logo))
        if selected is not None:
            self.play(self.goals.animate.fade_all_but(selected))
            self.play(Indicate(self.goals.submobjects[selected], color=ORANGE))
    
    def create_code_cell(self, position='LEFT', **kwargs) -> DynamicCode:
        cell = DynamicCode(**kwargs)
        if getattr(self, 'title', None):
            ytop = self.title.get_edge_center(DOWN)[1] - MARGIN
        else:
            ytop = config['top'][1] - MARGIN
        ybottom = config['bottom'][1] + MARGIN
        if position == 'LEFT':
            xleft = config['left_side'][0] + MARGIN
            xright = -MARGIN / 2
        elif position == 'RIGHT':
            xleft = MARGIN / 2
            xright = config['right_side'][0] - MARGIN
        elif position == 'FULL':
            xleft = config['left_side'][0] + MARGIN
            xright = config['right_side'][0] - MARGIN
        cell.set_background_size(xright - xleft, ytop - ybottom)
        cell.move_to(((xleft + xright) / 2, (ytop + ybottom) / 2, 0))
        return cell
    
    def store_mobjects(self):
        self._stored_mobjects = self.mobjects.copy()
    
    def restore_mobjects(self):
        self.mobjects = self._stored_mobjects
    
    def next_slide(self, *args, **kwargs):
        self.store_mobjects()
        self.wait()  # !? this appends a Mobject to self.mobjects that we don't need
        super().next_slide(*args, **kwargs)
        self.restore_mobjects()
