#from loderunnerclient.LodeRunnerClient import GameClient

from ctypes import cdll
lib = cdll.LoadLibrary('./cyth/libcyth.so')


from LodeRunnerClient import GameClient
import random
import logging
import os

import move

#from loderunnerclient.internals.actions import LoderunnerAction
#from loderunnerclient.internals.board import Board

from internals.actions import LoderunnerAction
from internals.board import Board
from internals.element import _ELEMENTS


logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s',
                    level=logging.INFO)


randstep = 1
pract = LoderunnerAction.DO_NOTHING
cntact=0

b=False
i=0
def turn(gcb: Board, strboard=""):
    global b
    global i
    global brd
    global randstep
    global pract
    global cntact
    #qq=lib.foo(strboard)
    print(strboard)
    brd = Board(strboard)
    #brd.print_board()
    #print("BARRIERS:\n",brd.get_barriers())
    #print("ME:\n",brd.get_my_position())
    #print("GOLD:",brd.get_gold_positions())
    print("STUFF:\n",brd.get_at(0,0))
    #print(brd.to_string())
    #print(lib.foo())
    #b=not b
    #return LoderunnerAction.DRILL_LEFT if b else LoderunnerAction.DRILL_RIGHT
    #action_id = random.randint(0, len(LoderunnerAction)-1)
    #act = list(LoderunnerAction)[action_id] if list(LoderunnerAction)[action_id] != LoderunnerAction.SUICIDE else LoderunnerAction.DO_NOTHING
    #return act

    #if [brd.get_my_position().get_x(),brd.get_my_position().get_y()] in brd.get_pipe_positions():
    #    print("PIPE")
    #    return LoderunnerAction.GO_DOWN
    if(randstep>0):
        print("GoRandom")
        randstep-=1
        action_id = random.randint(0, len(LoderunnerAction)-1)
        act = list(LoderunnerAction)[action_id] if list(LoderunnerAction)[action_id] != LoderunnerAction.SUICIDE else LoderunnerAction.DO_NOTHING
        return act
    else:
        _pos = brd.get_my_position()
        pos = [_pos.get_x(), _pos.get_y()]
        try:
            move.path_list=[]
            move.stack = []
            move.used = []
            move.new_used = []
            move.flag=False
            move.dfs(pos[0], pos[1], 0, brd)
            move.dfs_g(move.stack[0][0], move.stack[0][1], pos[0], pos[1], brd)
            print(move.path_list)
            print(move.stack)
            move.stack.sort(lambda x:x[2])

            to_coord = move.path_list[-move.stack[0][2]:][0]
        except:
            return random.choice((LoderunnerAction.GO_RIGHT, LoderunnerAction.GO_LEFT))
        if to_coord[0] > pos[0]:
            if pract==LoderunnerAction.GO_RIGHT:
                cntact+=1
                if(cntact==5):
                    randstep=4
                    cntact=0
            else:
                pract=LoderunnerAction.GO_RIGHT
                cntact=0
            return LoderunnerAction.GO_RIGHT
        elif to_coord[0] < pos[0]:
            if pract==LoderunnerAction.GO_LEFT:
                cntact+=1
                if(cntact==4):
                    randstep=4
                    cntact=0
            else:
                pract=LoderunnerAction.GO_LEFT
                cntact=0
            return LoderunnerAction.GO_LEFT
        elif to_coord[1] > pos[1]:
            if pract==LoderunnerAction.GO_UP:
                cntact+=1
                if(cntact==4):
                    randstep=4
                    cntact=0
            else:
                pract=LoderunnerAction.GO_UP
                cntact=0
            return LoderunnerAction.GO_UP
        else:
            if pract==LoderunnerAction.GO_DOWN:
                cntact+=1
                if(cntact==4):
                    randstep=4
                    cntact=0
            else:
                pract=LoderunnerAction.GO_DOWN
                cntact=0
            return LoderunnerAction.GO_DOWN



if __name__ == '__main__':

    url = "codingdojo2019.westeurope.cloudapp.azure.com"
    userId="jlebg3nx316vg6qfo6q1"
    userCode="7303406248495085684"
    #url = "codebattle-spb-2019.francecentral.cloudapp.azure.com"
    #userId="ocbpqfpr3dnpk82l0u5y"
    #userCode="1969960948607981448"

    #b="☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼                             ~~~~~~~~~          (~~~~~~~☼☼##H########################H#H     @ H##########H    $  ☼☼( H                        H######H  H      (   H#☼☼☼☼☼#☼☼H☼☼#☼☼H    H#########H (   H#&    H#####H#####H##((~~~~~☼☼H     H    H         H#####H#)    H ~   H  @  H @ЄЄ((  (☼☼H#☼#☼#H    H         H  ~~~ #####H#     H     H    ЄЄ(((☼☼H  ~  HЄ~Є~H~~~~~~   H         & H   H######H##     @ЄЄ(☼☼H  @  H    H     H###☼☼☼☼☼☼H☼ $  H~~~H      H         $#☼☼H   ( H    H#####H         H     H      H#########H $ @$☼☼☼###☼##☼##☼H         H###H##    H##     H#       ##     ☼☼☼###☼~~~~  H   & &   H   H######H######### H###H #####H#☼☼☼$((☼      H   ~~~~~~H   H      H          H# #H      H ☼☼########H###☼☼☼☼     H  ############   ###### ##########☼☼        H            H                      ((         @☼☼H##########################H########~~~####H############☼☼H                 ~~~      H    @          H $          ☼☼#######H#######            H###~~~~      ############H  ☼☼&      H~~~~~~~~~~         H                         H  ☼☼       H    ##H   #######H##########~~~~~~>H######## H  ☼☼ ((    H    ##H (        H     $   &       H         H  ☼☼##H#####    ########H#######~~~~  ~~~#########>~~~~  H  ☼☼  H      (          H    @                       ~~~ЄH $☼☼#########H##########H  $ @   #☼☼☼☼☼☼#   ☼☼☼☼☼☼☼      H  ☼☼((&      H          H        ~ (((((~     (          H  ☼☼☼☼&      H~~Є~~~~~~~H       « ######   ###########   H  ☼☼    H###### &       #######H           ~~~~~~~~~~~~~~H  ☼☼H☼  H         (            H  H####H )               H  ☼☼H☼☼#☼☼☼☼☼☼☼☼☼☼☼☼###☼☼☼☼☼☼☼☼H☼☼☼☼☼☼☼☼ ☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼#☼☼H $ @&       ~~H~~~~☼☼☼☼☼☼☼H☼☼☼☼☼☼☼       H @ ~~~~~~~~~H☼☼H~~~~  ###### &H       & H☼H☼H    (   ####H  ☼    $    H☼☼H       (   @  ##H#######H☼H☼H######H  &  ###☼☼☼☼☼☼☼☼ ~H☼☼H#########       H&   ~~~H☼H☼H~~~   H~~~~~ ##&(((((@ ~ H☼☼H        ###H####H##H (   ☼H☼       H     ###☼☼☼☼☼☼ ~  H☼☼H       &   H   @  #######☼H☼#####  H##### $ ~~~~~~~ ~ H☼☼~ЄЄ~~~~~~~~~H       H~~~~~☼H☼~~~~~  H             ~ ~  H☼☼  &  H              H ((($☼H☼     ##########H (        H☼☼ ### #############H H#####☼H☼               H ######## H☼☼H   (@            H     $$☼H☼#######   (    H @  (     H☼☼H#####         H##H####                ###H#########   H☼☼H      H######### H   ############        H            H☼☼H##    H          H~~~~~~                 H #######H## H☼☼~~~~#####H#   ~~~~H         ########H   & H    $ & H   H☼☼         H ►      H      ~~~~~~~~   H     H        H   H☼☼   ####### H   «######H##        ##############    H  (H☼☼           H(    $$   H        ~~~~~           ##H#####H☼☼H (  ###########H     H#####H      ( @H##H       H &   H☼☼H###            H(    H     ###########  ##H###  H     H☼☼H  ######  ##H######  H          (  $      H   ##H###  H☼☼H            H ~~~~~##H###H  @  #########H##           H☼☼    H########H#       H   ######         H    (        H☼☼ ###H        H         ~~~~~H      ##H###H####H###     H☼☼    H########H#########     H  @  (  H        H        H☼☼H   H                       H     (  H        H        H☼☼H  ####H######         #####H########H##      H#####   H☼☼H      H      H#######Q   (       (           H        H☼☼##############H    )  H#################################☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼"
    #br=Board(b)
    #br.print_board()
    #str = lib.foo(b)
    #print(":")
    #for c in _ELEMENTS:
    #    print(c,_ELEMENTS[c])
    '''print("\n")
    _pos = br.get_my_position()
    pos = [_pos.get_x(),_pos.get_y()]
    print("pos:\t",pos)
    print("\n")
    print(move.dfs(pos[0],pos[1],0,br))
    print(move.stack)
    move.dfs_g(move.stack[0][0], move.stack[0][1], pos[0],pos[1], br)
    to_coord = move.path_list[-move.stack[0][2]:][0]
    if to_coord[0] > pos[0]:
        return LoderunnerAction.GO_RIGHT
    elif to_coord[0] < pos[0]:
        return LoderunnerAction.GO_LEFT
    elif to_coord[1] > pos[1]:
        return LoderunnerAction.GO_UP
    else:
        return LoderunnerAction.GO_DOWN'''
    #print(move.path_list)
    gcb = GameClient(url, userId, userCode)
    gcb.run(turn)

