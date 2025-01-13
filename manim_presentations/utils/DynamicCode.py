from manim import *
from manim.mobject.text.text_mobject import remove_invisible_chars
import numpy as np
import re


class DynamicCode(VGroup):
    def __init__(self, *args, **kwargs):
        super().__init__()

        if "file_name" in kwargs:
            file_name = kwargs.pop("file_name")
            tmp_code = Code(file_name=file_name)
            kwargs["code"] = tmp_code.code_string
            kwargs["language"] = tmp_code.language
        elif "code" in kwargs:
            kwargs["code"] = kwargs["code"].strip('\n')
        
        if "clone_attrs_from" in kwargs:
            clone_attrs_from = kwargs.pop("clone_attrs_from")
            kwargs["tab_width"] = clone_attrs_from.tab_width
            kwargs["line_spacing"] = clone_attrs_from.line_spacing
            kwargs["font_size"] = clone_attrs_from.font_size
            kwargs["font"] = clone_attrs_from.font
            kwargs["margin"] = clone_attrs_from.margin
            kwargs["indentation_chars"] = clone_attrs_from.indentation_chars
            kwargs["background"] = clone_attrs_from.background
            kwargs["background_stroke_width"] = clone_attrs_from.background_stroke_width
            kwargs["background_stroke_color"] = clone_attrs_from.background_stroke_color
            kwargs["corner_radius"] = clone_attrs_from.corner_radius
            kwargs["insert_line_no"] = clone_attrs_from.insert_line_no
            kwargs["line_no_from"] = clone_attrs_from.line_no_from
            kwargs["line_no_buff"] = clone_attrs_from.line_no_buff
            kwargs["style"] = clone_attrs_from.style
            kwargs["language"] = clone_attrs_from.language
        
        # use a Code mobject to generate everything
        # then extract the background, any line numbers, and code elements
        tmp = Code(*args, **kwargs)
        self.background_mobject = tmp.background_mobject
        if hasattr(tmp, 'line_numbers'):
            self.line_numbers = tmp.line_numbers
            tmp.remove(tmp.line_numbers)
        else:
            self.line_numbers = VGroup()
        self.code = remove_invisible_chars(tmp.code)
        self.code_string = tmp.code_string
        tmp.remove(tmp.background_mobject, tmp.code)
        self.add(self.background_mobject, self.line_numbers, self.code)

        # copy attributes from Code object
        self.tab_width = tmp.tab_width
        self.line_spacing = tmp.line_spacing
        self.font_size = tmp.font_size
        self.font = tmp.font
        self.margin = tmp.margin
        self.indentation_chars = tmp.indentation_chars
        self.background = tmp.background
        self.background_stroke_width = tmp.background_stroke_width
        self.background_stroke_color = tmp.background_stroke_color
        self.corner_radius = tmp.corner_radius
        self.insert_line_no = tmp.insert_line_no
        self.line_no_from = tmp.line_no_from
        self.line_no_buff = tmp.line_no_buff
        self.style = tmp.style
        self.language = tmp.language

        # super().__init__(*args, **kwargs)
        # self.code = remove_invisible_chars(self.code)

        # # The self.code VGroup and the Paragraph submobject are not the same object
        # # which is enormously annoying when manipulating the code.
        # # They both contain the same characters, so we can get rid of one of them.
        # # We choose to replace the Paragraph submobject with the VGroup.
        # self.add(self.code)  # it's not a submobject be default???
        # for mobj in enumerate(self.submobjects):
        #     if isinstance(mobj, Paragraph):
        #         self.remove(mobj)
        #         break
    
    def set_background_width(self, width: float | str = 'auto'):
        # width = 'auto' -> fit to code width
        self.set_background_size(width=width, height=None)
    
    def set_background_height(self, height: float | str = 'auto'):
        # height = 'auto' -> fit to code height
        self.set_background_size(width=None, height=height)
    
    def set_background_size(self, width: float | str = None, height: float | str = None):
        if width is None and height is None:
            return
        if width == 'auto' or height == 'auto':
            x, y, w, h = self.get_code_bbox()
            if width == 'auto':
                width = w
            if height == 'auto':
                height = h
        bg = self.background_mobject
        mins = bg.points.min(axis=0)
        maxs = bg.points.max(axis=0)
        mids = (mins + maxs) / 2
        sizes = maxs - mins
        if width is not None:
            dw = width - sizes[0]
        if height is not None:
            dh = height - sizes[1]
        for i, pt in enumerate(bg.points):
            if width is not None and pt[0] > mids[0]:
                pt[0] += dw
            if height is not None and pt[1] < mids[1]:
                pt[1] -= dh
    
    def get_code_bbox(self, line_slice: slice = slice(None, None)) -> tuple[float, float]:
        foreground = VGroup(*self.code[line_slice])
        if self.insert_line_no:
            foreground.add(*self.line_numbers[line_slice])
        rect = SurroundingRectangle(foreground, buff=self.margin)
        return rect.x, rect.y, rect.width, rect.height
    
    def append_code(self, code: str, line_index: int = -1, opacity: float = 1, **kwargs):
        pos = (line_index, None) # None -> end of line
        self.insert_code(pos, code, opacity=opacity, **kwargs)
    
    def prepend_code(self, code: str, line_index: int = 0, opacity: float = 1, **kwargs):
        pos = (line_index, 0)
        self.insert_code(pos, code, opacity=opacity, **kwargs)
    
    def insert_code(self, pos: int | tuple[int | None, int | None] | None, code: str, opacity: float = 1, **kwargs):
        # if player is supplied, then play the insertion animations
        # otherwise just update the code instantly
        player: Scene = kwargs.pop('player', None)
        if player is not None:
            run_time = kwargs.pop('run_time', 1)
            lag_ratio = kwargs.pop('lag_ratio', 0.1)
            rt0 = min(0.5, run_time/2)
            rt1 = run_time - rt0
            pre_animation_mobjects = player.mobjects.copy()
            player.play(self.animate(run_time=rt0).insert_code(pos, code, rearrange_only=True, **kwargs))
            inserted_glyphs = self.insert_code(pos, code, opacity=0, **kwargs)
            player.play(inserted_glyphs.animate(run_time=rt1, lag_ratio=lag_ratio).set_opacity(opacity))
            post_animation_mobjects = player.mobjects.copy()
            
            # !!! Because the final animation creates new mobjects which make the prior references to these mobjects invalid.
            #     In addition, new mobjects are added to both player.mobjects and groups in player.pre_animation_mobjects
            #     which makes it difficult to remove these mobjects later as they must be removed from multiple groups.
            #     Totally crazy behavior to be sure, but as far as I can tell that's how it is for now.
            
            # The newly animated inserted glyphs appear to be in a group which is the last mobject in player.mobjects.
            # No idea how reliable this is, but it seems to work.
            new_glyphs = player.mobjects[-1]

            # Replace references to glyphs in self.code with references to the animated glyphs that replaced them.
            for i in range(len(self.code)):
                for j in range(len(self.code[i])):
                    for k in range(len(inserted_glyphs)):
                        if self.code[i][j] is inserted_glyphs[k]:
                            self.code[i][j] = new_glyphs[k]
                            break
            
            # The animation polluted player.mobjects with all sorts of extra objects and groups of objects which are not needed
            # as they are already in self. To clean up the scene heirarchy we need to remove these extra references.
            player.mobjects = pre_animation_mobjects
            return
        
        if len(self.code) > 0:
            lines = self.code_string.strip('\n').split('\n')
        else:
            lines = []

        line_index, char_index = self._get_char_pos(pos, lines)

        pre_lines = lines[:line_index]
        post_lines = lines[line_index:]
        if len(post_lines) > 0:
            insertion_line = post_lines.pop(0)
        else:
            insertion_line = ''
        pre_insert_string = insertion_line[:char_index]
        post_insert_string = insertion_line[char_index:]

        new_lines = (pre_insert_string + code + post_insert_string).split('\n')

        if code.startswith('\n') and char_index == len(insertion_line):
            pre_lines.append(new_lines.pop(0))
            insertion_line_changed = False
        elif code.endswith('\n') and char_index == 0:
            post_lines.insert(0, new_lines.pop(-1))
            insertion_line_changed = False
        else:
            insertion_line_changed = True
        
        if insertion_line_changed:
            # ignore whitespace to match glyph indices
            n_pre_insert_glyphs = len(re.sub(r'\s+', '', pre_insert_string))
            n_post_insert_glyphs = len(re.sub(r'\s+', '', post_insert_string))
            if n_pre_insert_glyphs:
                pre_insert_glyphs = self.code[line_index][:n_pre_insert_glyphs]
            if n_post_insert_glyphs:
                post_insert_glyphs = self.code[line_index][n_pre_insert_glyphs:]
        
        combined_lines = pre_lines + new_lines + post_lines
        combined_code = '\n'.join(combined_lines)

        tmp = DynamicCode(code=combined_code, clone_attrs_from=self)
        tmp.align_to(self, direction=UL)

        # if tmp.code.get_edge_center(UP)[1] < self.code.get_edge_center(UP)[1]:
        #     # in case self.code is scrolled up above background
        #     tmp.code.align_to(self.code, direction=UP)
        #     if self.insert_line_no:
        #         tmp.line_numbers.align_to(self.line_numbers, direction=UP)

        # create space for insertion
        autosize: bool = kwargs.pop('autosize', False)
        autowidth: bool = kwargs.pop('autowidth', False)
        autoheight: bool = kwargs.pop('autoheight', False)
        if autosize:
            self.set_background_size(tmp.background_mobject.width, tmp.background_mobject.height)
        elif autowidth:
            self.set_background_width(tmp.background_mobject.width)
        elif autoheight:
            self.set_background_height(tmp.background_mobject.height)
        
        if self.insert_line_no:
            # in case max number of digits in all line numbers changes
            if len(self.code):
                self.code.align_to(tmp.code, direction=LEFT)
        
        if insertion_line_changed and n_post_insert_glyphs > 0:
            # move post split glyphs to their new positions
            post_insert_glyphs.move_to(tmp.code[len(pre_lines)+len(new_lines)-1][-n_post_insert_glyphs:])
        
        if insertion_line_changed and n_pre_insert_glyphs > 0:
            # move pre split glyphs in case the new code slightly alters their vertical position
            pre_insert_glyphs.align_to(tmp.code[len(pre_lines)][:n_pre_insert_glyphs], UP)
        
        # shift pre lines up in case the new code slightly alters their vertical position
        if len(pre_lines) > 0:
            self.code[:len(pre_lines)].align_to(tmp.code, direction=UP)
        
        # shift post lines down to their new positions
        if len(post_lines) > 0:
            self.code[-len(post_lines):].align_to(tmp.code, direction=DOWN)
        
        if kwargs.pop('rearrange_only', False):
            return

        # extract new lines from tmp
        start_line_index = len(pre_lines)
        stop_line_index = start_line_index + len(new_lines)
        new_line_vgroups = tmp.code[start_line_index:stop_line_index]
        tmp.code.remove(*new_line_vgroups)
        new_line_vgroups.set_opacity(opacity)

        # color new glyphs?
        color = kwargs.pop('color', None)
        if color is not None:
            new_line_vgroups.set_color(color)

        # extract post split glyphs from self if needed
        if insertion_line_changed and n_post_insert_glyphs > 0:
            self.code[start_line_index].remove(*post_insert_glyphs)
        
        # insert extracted new lines into self
        inserted_glyphs = VGroup()
        for i, new_line_vgroup in enumerate(new_line_vgroups):
            line_index = start_line_index + i
            if i == 0 and insertion_line_changed and len(self.code) > line_index:
                # extract new glyphs from tmp and append to existing line in self
                new_glyphs_to_append = new_line_vgroup[n_pre_insert_glyphs:]
                if len(new_glyphs_to_append) > 0:
                    new_line_vgroup.remove(*new_glyphs_to_append)
                    self.code[line_index].add(*new_glyphs_to_append)
                    inserted_glyphs.add(*new_glyphs_to_append)
            elif i == len(new_line_vgroups) - 1 and insertion_line_changed and n_post_insert_glyphs > 0:
                # replace end of new line with extracted post split glyphs
                new_glyphs_to_be_replaced_with_existing_ones = new_line_vgroup[-n_post_insert_glyphs:]
                new_line_vgroup.remove(*new_glyphs_to_be_replaced_with_existing_ones)
                new_line_vgroup.add(*post_insert_glyphs)
                self.code.insert(line_index, new_line_vgroup)
                inserted_glyphs.add(*new_line_vgroup[:-n_post_insert_glyphs])
            else:
                self.code.insert(line_index, new_line_vgroup)
                inserted_glyphs.add(*new_line_vgroup[:])
        
        if self.insert_line_no:
            n_old_line_numbers = len(self.line_numbers)
            n_new_line_numbers = len(tmp.line_numbers)
            if n_new_line_numbers > n_old_line_numbers:
                # extract new line numbers from tmp and insert into self
                new_line_numbers = tmp.line_numbers[n_old_line_numbers:]
                tmp.line_numbers.remove(*new_line_numbers)
                self.line_numbers.add(*new_line_numbers)
                # ensure all old line numbers are right aligned
                for i in range(n_old_line_numbers):
                    self.line_numbers[i].align_to(tmp.line_numbers[i], direction=RIGHT)
        
        # update code_string
        self.code_string = tmp.code_string
        
        return inserted_glyphs
    
    def remove_code(self, start: int | tuple[int, int] = (0, 0), stop: int | tuple[int, int] = None, **kwargs):
        if start == (0, 0) and stop is None:
            self.clear_code()
            return
        
        # if player is supplied, then play the removal animations
        # otherwise just update the code instantly
        player: Scene = kwargs.pop('player', None)
        if player is not None:
            run_time = kwargs.pop('run_time', 1)
            player.play(self.animate(run_time=run_time).remove_code(start, stop, rearrange_only=True, **kwargs))
            self.remove_code(start, stop, **kwargs)
            return
        
        lines = self.code_string.strip('\n').split('\n')
        n_lines = len(lines)

        start_line_index, start_char_index = self._get_char_pos(start, lines)
        if stop is None:
            stop_line_index, stop_char_index = len(lines), 0
        else:
            stop_line_index, stop_char_index = self._get_char_pos(stop, lines)
        
        # ignore whitespace to match glyph indices
        start_glyph_index = len(re.sub(r'\s+', '', lines[start_line_index][:start_char_index]))
        if stop_line_index < n_lines:
            stop_glyph_index = len(re.sub(r'\s+', '', lines[stop_line_index][:stop_char_index]))
        else:
            stop_glyph_index = 0
        
        # updated code
        new_lines = lines.copy()
        if start_line_index == stop_line_index:
            new_lines[start_line_index] = new_lines[start_line_index][:start_char_index] + new_lines[start_line_index][stop_char_index:]
        else:
            new_lines[start_line_index] = new_lines[start_line_index][:start_char_index]
            if stop_line_index < n_lines:
                new_lines[start_line_index] += new_lines[stop_line_index][stop_char_index:]
            del new_lines[start_line_index+1:stop_line_index+1]
        
        new_code = '\n'.join(new_lines)

        tmp = DynamicCode(code=new_code, clone_attrs_from=self)
        tmp.align_to(self, direction=UL)

        # if tmp.code.get_edge_center(UP)[1] < self.code.get_edge_center(UP)[1]:
        #     # in case self.code is scrolled up above background
        #     tmp.code.align_to(self.code, direction=UP)
        #     if self.insert_line_no:
        #         tmp.line_numbers.align_to(self.line_numbers, direction=UP)

        # hide glyphs to be removed
        glyphs_to_be_removed = VGroup()
        lines_to_be_removed = VGroup()
        if start_line_index == stop_line_index:
            glyphs_to_be_removed = self.code[start_line_index][start_glyph_index:stop_glyph_index]
        else:
            for i in range(start_line_index, stop_line_index + 1):
                if i == start_line_index:
                    glyphs_to_be_removed = self.code[i][start_glyph_index:]
                elif i < n_lines:
                    if i == stop_line_index:
                        glyphs_to_be_removed.add(self.code[i][:stop_glyph_index])
                    else:
                        glyphs_to_be_removed.add(self.code[i][:])
                    lines_to_be_removed.add(self.code[i])
        glyphs_to_be_removed.set_opacity(0)

        if self.insert_line_no:
            # in case max number of digits in all line numbers changes
            self.code.align_to(tmp.code, direction=LEFT)
            self.line_numbers[:len(tmp.line_numbers)].align_to(tmp.line_numbers, direction=UR)
            # hide line numbers to be removed
            self.line_numbers[len(tmp.line_numbers):].set_opacity(0)

        # shift lines and glyphs
        if stop_line_index < n_lines:
            if stop_line_index != start_line_index:
                self.code[stop_line_index:].align_to(tmp.code, direction=DOWN)
            if stop_glyph_index < len(self.code[stop_line_index]):
                self.code[stop_line_index][stop_glyph_index:].align_to(tmp.code[start_line_index][start_glyph_index:], direction=LEFT)
        
        if self.insert_line_no:
            # in case max number of digits in all line numbers changes
            self.code.align_to(tmp.code, direction=LEFT)
        
        # shrink background?
        autosize: bool = kwargs.pop('autosize', False)
        autowidth: bool = kwargs.pop('autowidth', False)
        autoheight: bool = kwargs.pop('autoheight', False)
        if autosize:
            self.set_background_size(tmp.background_mobject.width, tmp.background_mobject.height)
        elif autowidth:
            self.set_background_width(tmp.background_mobject.width)
        elif autoheight:
            self.set_background_height(tmp.background_mobject.height)
        
        if kwargs.pop('rearrange_only', False):
            return

        # remove deleted lines/glyphs
        if start_line_index == stop_line_index:
            self.code[start_line_index].remove(*self.code[start_line_index][start_glyph_index:stop_glyph_index])
        else:
            self.code[start_line_index].remove(*self.code[start_line_index][start_glyph_index:])
            if stop_line_index < n_lines:
                self.code[start_line_index].add(*self.code[stop_line_index][stop_glyph_index:])
            self.code.remove(*lines_to_be_removed)

        if self.insert_line_no:
            self.line_numbers.remove(*self.line_numbers[len(tmp.line_numbers):])
        
        # update code_string
        self.code_string = tmp.code_string
    
    def clear_code(self):
        self.code.remove(*self.code.submobjects)
        self.code_string = ''
        if self.insert_line_no:
            self.line_numbers.remove(*self.line_numbers.submobjects)
    
    def set_code(self, code: str, **kwargs):
        self.clear_code()
        self.insert_code(0, code.strip('\n'), **kwargs)

    def scroll_to_last_line(self, **kwargs):
        if len(self.code) < 2:
            return
        
        # if player is supplied, then play the scroll animation
        # otherwise just update the code instantly
        player: Scene = kwargs.pop('player', None)
        if player is not None:
            run_time = kwargs.pop('run_time', 1)
            lag_ratio = 1.0 / (len(self.code) - 1)
            dy = self.code[0].get_edge_center(UP)[1] - self.code[-1].get_edge_center(UP)[1]
            pre_animation_mobjects = player.mobjects.copy()
            player.play(
                self.code[-1].animate(run_time=run_time).shift(dy * UP),
                FadeOut(self.code[:-1], run_time=run_time)#, lag_ratio=lag_ratio)
                # self.code[:-1].animate(run_time=run_time, lag_ratio=lag_ratio).set_opacity(0)
            )
            player.mobjects = pre_animation_mobjects
        else:
            self.code[-1].align_to(self.code[0], direction=UP)
        
        self.code.remove(*self.code[:-1])
        lines = self.code_string.strip('\n').split('\n')
        self.code_string = lines[-1]
    
    @staticmethod
    def _get_char_pos(pos: int | tuple[int, int], lines: list[str] | VGroup) -> tuple[int, int]:
        if len(lines) == 0:
            return 0, 0
        
        # pos -> line and char indices
        if isinstance(pos, int):
            # first char of line at pos
            line_index, char_index = pos, 0
        else:
            line_index, char_index = pos
        
        # None -> end of line
        if char_index is None:
            char_index = len(lines[line_index])
        
        # negative -> positive indices
        if line_index < 0:
            line_index = len(lines) + line_index
        if char_index < 0:
            char_index = len(lines[line_index]) + char_index
        
        return line_index, char_index
    
    # @staticmethod
    # def strip_multiline_initial_indent(code: str) -> str:
    #     if '\n' in code.strip('\n'):
    #         lines = code.split('\n')
    #         pos = lines[0].find(lines[0].lstrip())
    #         if pos > 0:
    #             lines = [line[pos:] for line in lines if len(line) > pos]
    #         code = '\n'.join(lines)
    #     return code


class DynamicCodeExampleScene(Scene):
    def construct(self):
        fresh = """
from manim import Scene, Square

class FadeInSquare(Scene):
    def construct(self):
        s = Square()
        self.play(FadeIn(s))
        self.play(s.animate.scale(2))
        self.wait()
"""
        
        code = DynamicCode(code=fresh, language="python", insert_line_no=False)
        code.to_edge(UL)
        self.add(code)

        insert = """\
pre
new line
new line
post\
"""
        code.insert_code((4, -1), insert, autosize=True, player=self, run_time=1)
        code.prepend_code(insert, autosize=True, player=self, run_time=1)
        code.append_code(insert, autosize=True, player=self, run_time=1)
        
        code.remove_code(0, (3, 2), autosize=True, player=self, run_time=1)
        code.remove_code(0, (0, 4), autosize=True, player=self, run_time=1)
        code.remove_code((4, -2), (7, -2), autosize=True, player=self, run_time=1)
        code.remove_code(-2, -1, autosize=True, player=self, run_time=1)
        
        # code.clear_code()
        code.set_code(fresh, autosize=True, player=self, run_time=1)

        self.wait(1)


if __name__ == "__main__":
    import os
    cmd = f"manim -pql {__file__} DynamicCodeExampleScene"
    os.system(cmd)