
from . import web
__author__ = '七月'


@web.route('/my/gifts')
def my_gifts():
    pass


@web.route('/gifts/book/<isbn>')
def save_to_gifts(isbn):
    # 赠书视图逻辑从这开始
    pass


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass



