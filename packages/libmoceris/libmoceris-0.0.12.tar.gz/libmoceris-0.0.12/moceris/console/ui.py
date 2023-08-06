import pygame
import moceris.console
def to_absolute_rect(rect):
    return [rect.x, rect.y, rect.x + rect.width - 1, rect.y + rect.height - 1]


def to_relative_rect(rect):
    return [rect.left, rect.top, rect.right - rect.left + 1, rect.bottom - rect.top + 1]


class Element:
    """
    一切 UI 控件的虚基类
    """

    CHILD_UPDATE = 1

    def __init__(self, class_name):
        """
        初始化

        :param class_name: 控件的类名，可以为 None，用于更新时对象间的交互
        """
        self.class_name = class_name
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.parent = None
        self.scene = None
        self.updated = True
        self.child_updated = True

    def display(self, *args) -> None:
        """
        绘制对象

        :param args: 备用，目前一般为空
        """
        pass

    def register(self,console, r_dict, rect, parent, scene) -> None:
        """
        向 Scene 注册本控件，不需要手动调用此函数

        欲重写该函数请参照基类格式

        :param console: Console 类的指针
        :param r_dict:  Scene 或上层 Element 传递的 class_name 字典引用
        :param rect: Scene 或上层 Element 传递的 rect，表示该元素将被限制在此 rect 内绘制（可以直接改 Console.rect 突破）
        :param parent: 父控件指针
        :param scene: 场景指针
        """
        self.rect = rect
        self.parent = parent
        self.scene = scene
        if self.class_name is not None:
            if self.class_name in r_dict:
                raise KeyError('class name:{0} existed.'.format(self.class_name))
            else:
                r_dict[self.class_name] = self

    def update(self, *args) -> None:
        """
        更新元素，通过 Scene 调用

        :param args: 用户定义的形参
        """
        pass

    def pass_up(self, signal):
        if signal == Element.CHILD_UPDATE:
            self.child_updated = True
        else:
            return
        if self.parent is not None:
            self.parent.pass_up(signal)


class FuncElement(Element):
    """
    对 Element 的简单封装，使用函数指针的方式简化构建，避免大量继承

    构建：提前定义 display 函数和 update 函数，参数为 (self,*args)，即控件指针和用户定义参数，然后在 init 中传入
    """

    def __init__(self, class_name, pt_display, pt_update):
        """
        初始化

        :param class_name: 同基类
        :param pt_display: display 的函数指针
        :param pt_update: update 的函数指针
        """
        Element.__init__(self, class_name)
        self.pt_display = pt_display
        self.pt_update = pt_update

    def display(self, *args):
        if self.pt_display is not None and self.updated:
            moceris.console.moprint.clear_rect()
            self.pt_display(self, *args)
            self.updated = False

    def update(self, *args):
        self.updated = True
        if self.pt_update is not None:
            self.pt_update(self, *args)
        self.pass_up(Element.CHILD_UPDATE)


class VerticalPanel(Element):
    """
    竖直排版
    """

    def __init__(self, class_name, n_child, s_child, have_border: bool, n_height):
        """
        初始化

        :param class_name: 同基类
        :param n_child: 上方子控件
        :param s_child: 下方子控件
        :param have_border: 是否显示边框
        :param n_height: 上方子控件的高度
        """
        Element.__init__(self, class_name)
        self.n_child = n_child
        self.s_child = s_child
        self.have_border = have_border
        self.n_height = n_height

    def register(self, console, r_dict, rect: pygame.Rect, parent, scene):
        super().register(console,r_dict, rect, parent, scene)
        if self.have_border:
            console._Console__draw_horizontal_border(self.rect.y + self.n_height, self.rect.x, self.rect.x + self.rect.width)
        self.n_child.register(console, r_dict, pygame.Rect(rect.x, rect.y, rect.width, self.n_height), self, scene)
        self.s_child.register(console, r_dict, pygame.Rect(rect.x, rect.y + self.n_height, rect.width,
                                                            rect.height - self.n_height), self, scene)

    def display(self, *args):
        if not self.child_updated:
            return
        self.child_updated = False
        if self.n_child is not None:
            moceris.console.moprint.set_rect(to_absolute_rect(self.n_child.rect))
            self.n_child.display(*args)
        if self.s_child is not None:
            moceris.console.moprint.set_rect(to_absolute_rect(self.s_child.rect))
            self.s_child.display(*args)


class HorizontalPanel(Element):
    """
    水平排版
    """

    def __init__(self, class_name, w_child, e_child, have_border: bool, w_width):
        """
        初始化

        :param class_name: 同基类
        :param w_child: 左方子控件
        :param e_child: 右方子控件
        :param have_border: 是否显示边框
        :param w_width: 左方子控件宽度
        """
        Element.__init__(self, class_name)
        self.w_child = w_child
        self.e_child = e_child
        self.have_border = have_border
        self.w_width = w_width

    def register(self, console, r_dict: dict, rect, parent, scene):
        super().register(console,r_dict, rect, parent, scene)
        if self.have_border:
            console._Console__draw_vertical_border(self.rect.x + self.w_width, self.rect.y, self.rect.y + self.rect.height)
        self.w_child.register(console, r_dict, pygame.Rect(rect.x, rect.y, self.w_width, rect.height), self, scene)
        self.e_child.register(console, r_dict,
                              pygame.Rect(rect.x + self.w_width, rect.y, rect.width - self.w_width,
                                          rect.height), self, scene)

    def display(self, *args):
        if not self.child_updated:
            return
        self.child_updated = False
        if self.w_child is not None:
            moceris.console.moprint.set_rect(to_absolute_rect(self.w_child.rect))
            self.w_child.display(*args)
        if self.e_child is not None:
            moceris.console.moprint.set_rect(to_absolute_rect(self.e_child.rect))
            self.e_child.display(*args)


class Scene:
    """
    场景类，将通过读 moceris.console.window 获得窗口大小并铺满全屏

    很傻逼且强制但是不想弄得太开
    """

    def __init__(self, layout):
        from moceris.console import this_console
        self.width = this_console.width
        self.height = this_console.height
        self.layout = layout
        self.element_dict = {}
        this_console._Console__clear_borders()
        self.layout.register(this_console,self.element_dict, pygame.Rect(0, 0, self.width, self.height), None, self)

    def display(self, *args) -> None:
        """
        绘制场景，由外部调用

        :param args: 暂时保留为空
        """
        from moceris.console import moprint
        moprint.default_rect()
        moprint.set_pos(0, 0)
        if self.layout is not None:
            self.layout.display(args)
        moprint.default_rect()

    def update(self, class_name, *args) -> None:
        """
        更新对象，可由外部调用也可用于控件之间传递信息

        :param class_name: 目标控件的类名
        :param args: 用户定义参数
        """
        if class_name not in self.element_dict:
            raise IndexError()
        self.element_dict[class_name].update(*args)

    def get_element(self, class_name) -> Element:
        if class_name not in self.element_dict:
            raise IndexError()
        return self.element_dict[class_name]
