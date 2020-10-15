import tkinter
import random
import math
import operator
import pygame


class MainReason:
    def __init__(self, main):
        self.main_screen()
        self.already = False
        self.already_two = False
        self.lng_of_list = 0
        self.font_name = ('Copperplate Gothic Bold', 17)
        self.font_in_game = ('Copperplate Gothic Bold', 21)
        main.bind('<Escape>', lambda event: main.destroy())

    def main_screen(self):
        self.lng_of_list = 0
        self.ttt_image = tkinter.PhotoImage(file='img/ttt_image_root.png')
        self.frame_ttt = tkinter.Label(image=self.ttt_image, bg='#fffdd0')
        self.frame_ttt.place(x=274.5, y=52)

        self.sng_player_img = tkinter.PhotoImage(file='img/single_player.png')
        self.sng_player_button = tkinter.Button(command=self.ch_single_pl, border=0, image=self.sng_player_img)
        self.sng_player_button.place(x=350, y=233)

        self.tw_player_img = tkinter.PhotoImage(file='img/two_players.png')
        self.tw_player_button = tkinter.Button(command=self.ch_two_pl, border=0, image=self.tw_player_img)
        self.tw_player_button.place(x=350, y=308)

        self.scr_image = tkinter.PhotoImage(file='img/score_button.png')
        self.scr_button = tkinter.Button(command=self.cont_to_list_scores, border=0, image=self.scr_image)
        self.scr_button.place(x=772, y=336.43)

    def cont_to_list_scores(self):
        self.dest_init()
        self.only_list_of_scores('menu')

    def dest_init(self):
        self.frame_ttt.destroy()
        self.sng_player_button.destroy()
        self.tw_player_button.destroy()
        self.scr_button.destroy()

    def dest_sng(self, event):
        self.bc_buttn.destroy()
        self.single_pl_canvas.place_forget()
        self.tyn_img_lb.destroy()
        self.enr_sgl_pl.destroy()
        self.button_apply_sng.destroy()
        self.button_cc_sng.destroy()
        if self.already == True:
            self.canvas_att.destroy()
            self.already = False
        if event != 'noevent':
            self.main_screen()

    def dest_two(self, event):
        self.bc_buttn.destroy()
        self.single_pl_canvas.place_forget()
        self.tyn_img_lb.destroy()
        self.enr_sgl_pl.destroy()
        self.button_apply_sng.destroy()
        self.button_cc_sng.destroy()
        self.two_pl_canvas.place_forget()
        self.enr_sgl_two.destroy()
        self.button_cc_two.destroy()
        if self.already == True:
            self.canvas_att.destroy()
            self.already = False
        if self.already_two == True:
            self.canvas_att_two.destroy()
            self.already_two = False
        if event != 'noevent':
            self.main_screen()

    def dest_score(self, event='no'):
        self.bc_buttn.destroy()
        self.only_list_scores.destroy()
        self.dest_init()
        self.main_screen()

    def bck_buttn(self, mode='one'):
        bc_img = tkinter.PhotoImage(file='img/back_button.png')
        self.bc_buttn = tkinter.Canvas(width=48, height=38, highlightthickness=0, bg='#fffdd0')
        self.bc_buttn.create_image(22, 17, image=bc_img)
        self.bc_buttn.photo = bc_img
        self.bc_buttn.place(x=10, y=13.57)
        if mode == 'one':
            self.bc_buttn.bind('<Button-1>', self.dest_sng)
        elif mode == 'two':
            self.bc_buttn.bind('<Button-1>', self.dest_two)
        elif mode == 'score':
            self.bc_buttn.bind('<Button-1>', self.dest_score)

    def usr_ava(self, x_=0.0, y_=0.0, mode='one'):
        bg_clr = '#%02x%02x%02x' % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        outline_clr = '#%02x%02x%02x' % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        fillpl_clr = '#%02x%02x%02x' % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        outlineov_clr = '#%02x%02x%02x' % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        fillplov_clr = '#%02x%02x%02x' % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        if mode == 'one':
            self.single_pl_canvas = tkinter.Canvas(width=200, height=200, bg=bg_clr, highlightbackground="black")
            self.plgn = self.single_pl_canvas.create_polygon(5, 182.5, 195, 182.5, 150, 112.5, 100, 132.5, 50, 112.5, smooth=1, outline=outline_clr, width=5, fill=fillpl_clr)
            self.ovl = self.single_pl_canvas.create_oval(60, 17.5, 140, 112.5, outline=outlineov_clr, width=5, fill=fillplov_clr)
            self.single_pl_canvas.place(x=x_, y=y_)
        else:
            self.two_pl_canvas = tkinter.Canvas(width=200, height=200, bg=bg_clr, highlightbackground="black")
            self.plgn_two = self.two_pl_canvas.create_polygon(5, 182.5, 195, 182.5, 150, 112.5, 100, 132.5, 50, 112.5, smooth=1, outline=outline_clr, width=5, fill=fillpl_clr)
            self.ovl_two = self.two_pl_canvas.create_oval(60, 17.5, 140, 112.5, outline=outlineov_clr, width=5, fill=fillplov_clr)
            self.two_pl_canvas.place(x=x_, y=y_)

    def tyn_label(self, x_=0.0, y_=0.0, mode='one'):
        if mode == 'one':
            tyn_img = tkinter.PhotoImage(file='img/tyn.png')
            self.tyn_img_lb = tkinter.Label(image=tyn_img, bg='#fffdd0')
            self.tyn_img_lb.photo = tyn_img
            self.tyn_img_lb.place(x=x_, y=y_)
        else:
            tyn_img = tkinter.PhotoImage(file='img/tyns.png')
            self.tyn_img_lb = tkinter.Label(image=tyn_img, bg='#fffdd0')
            self.tyn_img_lb.photo = tyn_img
            self.tyn_img_lb.place(x=x_, y=y_)

    def entr_sps(self, x_=0.0, y_=0.0, mode='one'):
        def limits(*args):
            max_lng = 10
            '''
            if self.var.get() == 'Mistake':
                self.dest_sng('noevent')
                self.win_screen()
            '''
            if len(self.var.get()) > max_lng:
                self.var.set(self.var.get()[:max_lng])
            if not self.var.get().isalpha():
                self.var.set(''.join(filter(str.isalpha, self.var.get())))
            if self.var.get()[0:1].islower() and self.var.get()[0:1].isalpha():
                self.var.set(self.var.get()[0].upper())
            if self.var.get()[1:].isalpha():
                ln = self.var.get()[0].upper() + self.var.get()[1:].lower()
                self.var.set(ln)

        def limits_two(*args):
            max_lng = 10
            if len(self.var_two.get()) > max_lng:
                self.var_two.set(self.var_two.get()[:max_lng])
            if not self.var_two.get().isalpha():
                self.var_two.set(''.join(filter(str.isalpha, self.var_two.get())))
            if self.var_two.get()[0:1].islower() and self.var_two.get()[0:1].isalpha():
                self.var_two.set(self.var_two.get()[0].upper())
            if self.var_two.get()[1:].isalpha():
                ln = self.var_two.get()[0].upper() + self.var_two.get()[1:].lower()
                self.var_two.set(ln)


        if mode == 'one':
            self.var = tkinter.StringVar()
            self.var.trace('w', limits)
            self.enr_sgl_pl = tkinter.Entry(bd=2, justify=tkinter.CENTER, font=self.font_name, selectbackground='dodger blue', selectforeground='yellow2', fg='black', highlightbackground='blue', relief=tkinter.GROOVE, textvariable=self.var)
            self.enr_sgl_pl.place(x=x_, y=y_, height=34, width=181)
        else:
            self.var_two = tkinter.StringVar()
            self.var_two.trace('w', limits_two)
            self.enr_sgl_two = tkinter.Entry(bd=2, justify=tkinter.CENTER, font=self.font_name, selectbackground='dodger blue', selectforeground='yellow2', fg='black',highlightbackground='blue', relief=tkinter.GROOVE, textvariable=self.var_two)
            self.enr_sgl_two.place(x=x_, y=y_, height=34, width=181)

    def bttn_app(self, x_=0.0, y_=0.0, mode='one'):
        button_apply_img = tkinter.PhotoImage(file='img/apply_button.png')
        if mode == 'one':
            self.button_apply_sng = tkinter.Button(bd=0, image=button_apply_img, command=self.appling_one)
            self.button_apply_sng.photo = button_apply_img
            self.button_apply_sng.place(x=x_, y=y_)
        else:
            self.button_apply_sng = tkinter.Button(bd=0, image=button_apply_img, command=self.appling_two)
            self.button_apply_sng.photo = button_apply_img
            self.button_apply_sng.place(x=x_, y=y_)

    def appling_two(self):
        canvas_att_img = tkinter.PhotoImage(file='img/attention_button.png')
        if len(self.var.get()) < 2 or (self.var.get() == self.var_two.get()) or self.var.get() == 'Bot':
            if self.already == False:
                self.canvas_att = tkinter.Canvas(bg='#fffdd0', width=8, height=18, highlightthickness=0)
                self.canvas_att.create_image(5, 10, image=canvas_att_img)
                self.canvas_att.photo = canvas_att_img
                self.canvas_att.place(x=428, y=143.5)
                self.already = True
        else:
            if self.already == True:
                self.canvas_att.destroy()
                self.already = False
        if len(self.var_two.get()) < 2 or (self.var_two.get() == self.var.get()) or self.var_two.get() == 'Bot':
            if self.already_two == False:
                self.canvas_att_two = tkinter.Canvas(bg='#fffdd0', width=8, height=18, highlightthickness=0)
                self.canvas_att_two.create_image(5, 10, image=canvas_att_img)
                self.canvas_att_two.photo = canvas_att_img
                self.canvas_att_two.place(x=657, y=143.5)
                self.already_two = True
        else:
            if self.already_two == True:
                self.canvas_att_two.destroy()
                self.already_two = False
        if self.already_two == False and self.already == False:
            self.dest_two('noevent')
            self.start_game('two')

    def appling_one(self):
        if len(self.var.get()) < 2 or self.var.get() == 'Bot':
            if self.already == False:
                canvas_att_img = tkinter.PhotoImage(file='img/attention_button.png')
                self.canvas_att = tkinter.Canvas(bg='#fffdd0', width=8, height=18, highlightthickness=0)
                self.canvas_att.create_image(5, 10, image=canvas_att_img)
                self.canvas_att.photo = canvas_att_img
                self.canvas_att.place(x=667, y=143.5)
                self.already = True
        else:
            if self.already == True:
                self.canvas_att.destroy()
                self.already = False
        if self.already == False:
            self.dest_sng('noevent')
            self.start_game('one')

    def chc_one(self):
        self.single_pl_canvas.configure(bg='#%02x%02x%02x' % (random.randint(0, 255), random.randint(0, 255),random.randint(0, 255)))
        self.single_pl_canvas.itemconfigure(self.plgn, outline='#%02x%02x%02x' % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), fill='#%02x%02x%02x' % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        self.single_pl_canvas.itemconfigure(self.ovl, outline='#%02x%02x%02x' % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), fill='#%02x%02x%02x' % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    def chc_two(self):
        self.two_pl_canvas.configure(bg='#%02x%02x%02x' % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        self.two_pl_canvas.itemconfigure(self.plgn_two, outline='#%02x%02x%02x' % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), fill='#%02x%02x%02x' % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        self.two_pl_canvas.itemconfigure(self.ovl_two, outline='#%02x%02x%02x' % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), fill='#%02x%02x%02x' % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    def bttn_chc(self, x_=0.0, y_=0.0, mode='one'):
        button_cc_img = tkinter.PhotoImage(file='img/change_color_button.png')

        if mode == 'one':
            self.button_cc_sng = tkinter.Button(bd=0, image=button_cc_img, command=self.chc_one)
            self.button_cc_sng.photo = button_cc_img
            self.button_cc_sng.place(x=x_, y=y_)
        else:
            self.button_cc_two = tkinter.Button(bd=0, image=button_cc_img, command=self.chc_two)
            self.button_cc_two.photo = button_cc_img
            self.button_cc_two.place(x=x_, y=y_)

    def ch_single_pl(self):
        self.dest_init()
        self.bck_buttn('one')
        self.usr_ava(221, 62.5, 'one')
        self.tyn_label(471, 81.5, 'one')
        self.entr_sps(484, 134.5, 'one')
        self.bttn_app(520.5, 203.5, 'one')
        self.bttn_chc(221, 297.5, 'one')

    def ch_two_pl(self):
        self.dest_init()
        self.bck_buttn('two')
        self.usr_ava(10, 62.5, 'one')
        self.bttn_chc(10, 297.5, 'one')
        self.usr_ava(690, 62.5, 'two')
        self.bttn_chc(690, 297.5, 'two')
        self.tyn_label(343, 81.5, 'two')
        self.entr_sps(245, 134.5, 'one')
        self.entr_sps(474, 134.5, 'two')
        self.bttn_app(396, 203.5, 'two')

    def main_grid_func(self, x_=0.0, y_=0.0):
        main_grid_img = tkinter.PhotoImage(file='img/main_grid.png')
        self.main_grid = tkinter.Canvas(width=376, height=376, highlightthickness=0, bg='#fffdd0')
        self.main_grid.create_image(188, 188, image=main_grid_img)
        self. main_grid.photo = main_grid_img
        self.main_grid.place(x=x_, y=y_)

        self.cross = tkinter.PhotoImage(file='img/cross.png')
        self.round = tkinter.PhotoImage(file='img/round.png')

        self.cell_zero = tkinter.Canvas(root, width=122, height=122, highlightthickness=0, bg='#fffdd0')
        self.zero = self.cell_zero.create_image(61, 61)
        self.cell_zero.place(x=262, y=12)

        self.cell_one = tkinter.Canvas(width=122, height=122, highlightthickness=0, bg='#fffdd0')
        self.cell_one.place(x=389, y=12)
        self.one = self.cell_one.create_image(61, 61)

        self.cell_two = tkinter.Canvas(width=122, height=122, highlightthickness=0, bg='#fffdd0')
        self.cell_two.place(x=516, y=12)
        self.two = self.cell_two.create_image(61, 61)

        self.cell_three = tkinter.Canvas(width=122, height=122, highlightthickness=0, bg='#fffdd0')
        self.cell_three.place(x=262, y=139)
        self.three = self.cell_three.create_image(61, 61)

        self.cell_four = tkinter.Canvas(width=122, height=122, highlightthickness=0, bg='#fffdd0')
        self.cell_four.place(x=389, y=139)
        self.four = self.cell_four.create_image(61, 61)

        self.cell_five = tkinter.Canvas(width=122, height=122, highlightthickness=0, bg='#fffdd0')
        self.cell_five.place(x=516, y=139)
        self.five = self.cell_five.create_image(61, 61)

        self.cell_six = tkinter.Canvas(width=122, height=122, highlightthickness=0, bg='#fffdd0')
        self.cell_six.place(x=262, y=266)
        self.six = self.cell_six.create_image(61, 61)

        self.cell_seven = tkinter.Canvas(width=122, height=122, highlightthickness=0, bg='#fffdd0')
        self.cell_seven.place(x=389, y=266)
        self.seven = self.cell_seven.create_image(61, 61)

        self.cell_eight = tkinter.Canvas(width=122, height=122, highlightthickness=0, bg='#fffdd0')
        self.cell_eight.place(x=516, y=266)
        self.eight = self.cell_eight.create_image(61, 61)

    def name_tag_func(self, x_=0.0, y_=0.0, mode='one'):

        if mode == 'one':
            self.name_tag_one = tkinter.Canvas(width=200, height=40, bg='#fffdd0', highlightthickness=0)
            self.nto = self.name_tag_one.create_text(100, 20, font=self.font_in_game, text=self.var.get(), anchor=tkinter.CENTER, fill='firebrick3')
            self.name_tag_one.place(x=x_, y=y_)
        elif mode == 'bot':
            self.name_tag_two = tkinter.Canvas(width=200, height=40, bg='#fffdd0', highlightthickness=0)
            self.ntt = self.name_tag_two.create_text(100, 20, font=self.font_in_game, text='Bot', anchor=tkinter.CENTER, fill='firebrick3')
            self.name_tag_two.place(x=x_, y=y_)
        else:
            self.name_tag_two = tkinter.Canvas(width=200, height=40, bg='#fffdd0', highlightthickness=0)
            self.ntt = self.name_tag_two.create_text(100, 20, font=self.font_in_game, text=self.var_two.get(), anchor=tkinter.CENTER, fill='firebrick3')
            self.name_tag_two.place(x=x_, y=y_)

    def chosing_first_turn(self):
        num_canvas = tkinter.Canvas(width=376, height=376, highlightthickness=0)
        num_image = tkinter.PhotoImage(file='img/num3.png')
        noon = num_canvas.create_image(188, 188, image=num_image)
        num_canvas.photo = num_image
        num_canvas.place(x=262, y=12)
        def twostep():
            num_image_two = tkinter.PhotoImage(file='img/num2.png')
            num_canvas.itemconfigure(noon, image=num_image_two)
            num_canvas.photo = num_image_two
            def thirdstep():
                num_image_three = tkinter.PhotoImage(file='img/num1.png')
                num_canvas.itemconfigure(noon, image=num_image_three)
                num_canvas.photo = num_image_three
                def laststep():
                    if self.side == 0:
                        arrow_to_left_image = tkinter.PhotoImage(file='img/left.png')
                        num_canvas.itemconfigure(noon, image=arrow_to_left_image)
                        num_canvas.photo = arrow_to_left_image
                    else:
                        arrow_to_right_image = tkinter.PhotoImage(file='img/right.png')
                        num_canvas.itemconfigure(noon, image=arrow_to_right_image)
                        num_canvas.photo = arrow_to_right_image
                    root.after(1500, lambda: num_canvas.destroy())
                root.after(750, laststep)
            root.after(750, thirdstep)
        root.after(750, twostep)

    def your_turn_label(self):
        self.canvas_turn_tag = tkinter.Canvas(width=200, height=40, bg='#fffdd0', highlightthickness=0)
        self.canvas_turn_tag.create_text(100, 20, font=self.font_in_game, text='Your turn', anchor=tkinter.CENTER, fill='gray20')
        if self.side == 0:
            self.canvas_turn_tag.place(x=10, y=310)
        else:
            self.canvas_turn_tag.place(x=690, y=310)

    def changing_side(self):
        if self.current_side == 0:
            self.canvas_turn_tag.place_forget()
            self.canvas_turn_tag.place(x=690, y=310)
            self.current_side = 1
        elif self.current_side == 1:
            self.canvas_turn_tag.place_forget()
            self.canvas_turn_tag.place(x=10, y=310)
            self.current_side = 0

    def paint(self, cell='zero'):
        if self.current == 1 and cell in self.current_results:
            if cell == 'zero':
                self.cell_zero.itemconfigure(self.zero, image=self.cross)
                self.current_results[0] = 'X'
                self.changing_side()
            elif cell == 'one':
                self.cell_one.itemconfigure(self.one, image=self.cross)
                self.current_results[1] = 'X'
                self.changing_side()
            elif cell == 'two':
                self.cell_two.itemconfigure(self.two, image=self.cross)
                self.current_results[2] = 'X'
                self.changing_side()
            elif cell == 'three':
                self.cell_three.itemconfigure(self.three, image=self.cross)
                self.current_results[3] = 'X'
                self.changing_side()
            elif cell == 'four':
                self.cell_four.itemconfigure(self.four, image=self.cross)
                self.current_results[4] = 'X'
                self.changing_side()
            elif cell == 'five':
                self.cell_five.itemconfigure(self.five, image=self.cross)
                self.current_results[5] = 'X'
                self.changing_side()
            elif cell == 'six':
                self.cell_six.itemconfigure(self.six, image=self.cross)
                self.current_results[6] = 'X'
                self.changing_side()
            elif cell == 'seven':
                self.cell_seven.itemconfigure(self.seven, image=self.cross)
                self.current_results[7] = 'X'
                self.changing_side()
            elif cell == 'eight':
                self.cell_eight.itemconfigure(self.eight, image=self.cross)
                self.current_results[8] = 'X'
                self.changing_side()
            self.current = 0
            self.pick()
        elif self.current == 0 and cell in self.current_results:
            if cell == 'zero':
                self.cell_zero.itemconfigure(self.zero, image=self.round)
                self.current_results[0] = 'O'
                self.changing_side()
            elif cell == 'one':
                self.cell_one.itemconfigure(self.one, image=self.round)
                self.current_results[1] = 'O'
                self.changing_side()
            elif cell == 'two':
                self.cell_two.itemconfigure(self.two, image=self.round)
                self.current_results[2] = 'O'
                self.changing_side()
            elif cell == 'three':
                self.cell_three.itemconfigure(self.three, image=self.round)
                self.current_results[3] = 'O'
                self.changing_side()
            elif cell == 'four':
                self.cell_four.itemconfigure(self.four, image=self.round)
                self.current_results[4] = 'O'
                self.changing_side()
            elif cell == 'five':
                self.cell_five.itemconfigure(self.five, image=self.round)
                self.current_results[5] = 'O'
                self.changing_side()
            elif cell == 'six':
                self.cell_six.itemconfigure(self.six, image=self.round)
                self.current_results[6] = 'O'
                self.changing_side()
            elif cell == 'seven':
                self.cell_seven.itemconfigure(self.seven, image=self.round)
                self.current_results[7] = 'O'
                self.changing_side()
            elif cell == 'eight':
                self.cell_eight.itemconfigure(self.eight, image=self.round)
                self.current_results[8] = 'O'
                self.changing_side()
            self.current = 1
            self.pick()

    def check_status(self):
        if self.current_results[0] == self.current_results[1] == self.current_results[2]:
            self.wwoonn = 1
            self.results()
        elif self.current_results[3] == self.current_results[4] == self.current_results[5]:
            self.wwoonn = 1
            self.results()
        elif self.current_results[6] == self.current_results[7] == self.current_results[8]:
            self.wwoonn = 1
            self.results()
        elif self.current_results[0] == self.current_results[3] == self.current_results[6]:
            self.wwoonn = 1
            self.results()
        elif self.current_results[1] == self.current_results[4] == self.current_results[7]:
            self.wwoonn = 1
            self.results()
        elif self.current_results[2] == self.current_results[5] == self.current_results[8]:
            self.wwoonn = 1
            self.results()
        elif self.current_results[0] == self.current_results[4] == self.current_results[8]:
            self.wwoonn = 1
            self.results()
        elif self.current_results[2] == self.current_results[4] == self.current_results[6]:
            self.wwoonn = 1
            self.results()
        elif self.current_results[0] != 'zero' and self.current_results[1] != 'one' and self.current_results[2] != 'two' and self.current_results[3] != 'three' and self.current_results[4] != 'four' and self.current_results[5] != 'five' and self.current_results[6] != 'six' and self.current_results[7] != 'seven' and self.current_results[8] != 'eight':
            self.wwoonn = 1
            self.rslt = '='
            self.results()

    def pick(self):
        self.check_status()
        if self.entity == 'bot' and self.current_side == 1 and self.wwoonn == 0:
            if self.current_results[0] == self.current_results[1] and 'two' in self.current_results:
                self.paint('two')
            elif self.current_results[0] == self.current_results[2] and 'one' in self.current_results:
                self.paint('one')
            elif self.current_results[2] == self.current_results[1] and 'zero' in self.current_results:
                self.paint('zero')
            elif self.current_results[3] == self.current_results[4] and 'five' in self.current_results:
                self.paint('five')
            elif self.current_results[3] == self.current_results[5] and 'four' in self.current_results:
                self.paint('four')
            elif self.current_results[5] == self.current_results[4] and 'three' in self.current_results:
                self.paint('three')
            elif self.current_results[6] == self.current_results[7] and 'eight' in self.current_results:
                self.paint('eight')
            elif self.current_results[6] == self.current_results[8] and 'seven' in self.current_results:
                self.paint('seven')
            elif self.current_results[8] == self.current_results[7] and 'six' in self.current_results:
                self.paint('six')
            elif self.current_results[0] == self.current_results[3] and 'six' in self.current_results:
                self.paint('six')
            elif self.current_results[3] == self.current_results[6] and 'zero' in self.current_results:
                self.paint('zero')
            elif self.current_results[6] == self.current_results[0] and 'three' in self.current_results:
                self.paint('three')
            elif self.current_results[2] == self.current_results[5] and 'eight' in self.current_results:
                self.paint('eight')
            elif self.current_results[5] == self.current_results[8] and 'two' in self.current_results:
                self.paint('two')
            elif self.current_results[8] == self.current_results[2] and 'five' in self.current_results:
                self.paint('five')
            elif self.current_results[1] == self.current_results[4] and 'seven' in self.current_results:
                self.paint('seven')
            elif self.current_results[4] == self.current_results[7] and 'one' in self.current_results:
                self.paint('one')
            elif self.current_results[7] == self.current_results[1] and 'four' in self.current_results:
                self.paint('four')
            elif self.current_results[0] == self.current_results[4] and 'eight' in self.current_results:
                self.paint('eight')
            elif self.current_results[4] == self.current_results[8] and 'zero' in self.current_results:
                self.paint('zero')
            elif self.current_results[8] == self.current_results[0] and 'four' in self.current_results:
                self.paint('four')
            elif self.current_results[2] == self.current_results[4] and 'six' in self.current_results:
                self.paint('six')
            elif self.current_results[4] == self.current_results[6] and 'two' in self.current_results:
                self.paint('two')
            elif self.current_results[6] == self.current_results[2] and 'four' in self.current_results:
                self.paint('four')
            else:
                while self.current_results[0] == 'zero' or self.current_results[1] == 'one' or self.current_results[2] == 'two' or self.current_results[3] == 'three' or self.current_results[4] == 'four' or self.current_results[5] == 'five' or self.current_results[6] == 'six' or self.current_results[7] == 'seven' or self.current_results[8] == 'eight':
                    pico = random.randint(0, 8)
                    if pico == 0 and self.current_results[0] == 'zero':
                        self.paint('zero')
                        break
                    elif pico == 1 and self.current_results[1] == 'one':
                        self.paint('one')
                        break
                    elif pico == 2 and self.current_results[2] == 'two':
                        self.paint('two')
                        break
                    elif pico == 3 and self.current_results[3] == 'three':
                        self.paint('three')
                        break
                    elif pico == 4 and self.current_results[4] == 'four':
                        self.paint('four')
                        break
                    elif pico == 5 and self.current_results[5] == 'five':
                        self.paint('five')
                        break
                    elif pico == 6 and self.current_results[6] == 'six':
                        self.paint('six')
                        break
                    elif pico == 7 and self.current_results[7] == 'seven':
                        self.paint('seven')
                        break
                    elif pico == 8 and self.current_results[8] == 'eight':
                        self.paint('eight')
                        break
        else:
            self.cell_zero.bind('<Button-1>', lambda x: self.paint('zero'))
            self.cell_one.bind('<Button-1>', lambda x: self.paint('one'))
            self.cell_two.bind('<Button-1>', lambda x: self.paint('two'))
            self.cell_three.bind('<Button-1>', lambda x: self.paint('three'))
            self.cell_four.bind('<Button-1>', lambda x: self.paint('four'))
            self.cell_five.bind('<Button-1>', lambda x: self.paint('five'))
            self.cell_six.bind('<Button-1>', lambda x: self.paint('six'))
            self.cell_seven.bind('<Button-1>', lambda x: self.paint('seven'))
            self.cell_eight.bind('<Button-1>', lambda x: self.paint('eight'))

    def results(self):
        self.cell_eight.delete(tkinter.ALL)
        self.cell_eight.place_forget()
        self.cell_seven.delete(tkinter.ALL)
        self.cell_seven.place_forget()
        self.cell_six.delete(tkinter.ALL)
        self.cell_six.place_forget()
        self.cell_five.delete(tkinter.ALL)
        self.cell_five.place_forget()
        self.cell_four.delete(tkinter.ALL)
        self.cell_four.place_forget()
        self.cell_three.delete(tkinter.ALL)
        self.cell_three.place_forget()
        self.cell_two.delete(tkinter.ALL)
        self.cell_two.place_forget()
        self.cell_one.delete(tkinter.ALL)
        self.cell_one.place_forget()
        self.cell_zero.delete(tkinter.ALL)
        self.cell_zero.place_forget()
        self.main_grid.destroy()
        self.canvas_turn_tag.destroy()

        self.name_tag_one.place_forget()
        self.name_tag_two.place_forget()

        self.two_pl_canvas.place_forget()
        self.single_pl_canvas.place_forget()
        self.win_screen()

    def win_screen(self):
        cont_image = tkinter.PhotoImage(file='img/continue_button.png')
        self.continue_button = tkinter.Button(border=0, highlightbackground='red', image=cont_image, relief=tkinter.RIDGE, command=self.score_list)
        self.continue_button.photo = cont_image

        self.win_canvas = tkinter.Canvas(width=900, height=400, highlightthickness=0, bg='#fffdd0')
        self.win_canvas.pack()
        self.x = 0
        self.x2 = 12.45
        self.count = 0
        def sin_cos():
            if self.count < 310:
                y1 = -math.cos(self.x)
                y2 = math.cos(self.x)
                if self.count % 2 == 0:
                    self.win_canvas.create_oval(72 * self.x, 150 * y1 + 200, 72 * self.x, 150 * y1 + 200, width=19, outline='#%02x%02x%02x' % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
                    self.win_canvas.create_oval(72 * self.x, 150 * y2 + 200, 72 * self.x, 150 * y2 + 200, width=19, outline='#%02x%02x%02x' % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
                    self.win_canvas.create_oval(72 * self.x2, 150 * y1 + 200, 72 * self.x2, 150 * y1 + 200, width=19, outline='#%02x%02x%02x' % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
                    self.win_canvas.create_oval(72 * self.x2, 150 * y2 + 200, 72 * self.x2, 150 * y2 + 200, width=19, outline='#%02x%02x%02x' % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
                self.x += 0.02
                self.x2 -= 0.02
                self.count += 1
                root.after(5, sin_cos)
            else:
                if self.rslt == '=':
                    self.name_tag_one.configure(bg='snow2', bd=1, highlightbackground='red', highlightthickness=1)
                    self.name_tag_one.place(x=240, y=50)
                    tkinter.Misc.lift(self.name_tag_one)
                    self.name_tag_two.configure(bg='snow2', bd=1, highlightbackground='red', highlightthickness=1)
                    self.name_tag_two.place(x=460, y=50)
                    tkinter.Misc.lift(self.name_tag_two)

                    self.single_pl_canvas.place(x=240, y=100)
                    tkinter.Misc.lift(self.single_pl_canvas)
                    self.two_pl_canvas.place(x=460, y=100)
                    tkinter.Misc.lift(self.two_pl_canvas)

                    self.continue_button.place(x=350, y=310)
                    tkinter.Misc.lift(self.continue_button)
                elif self.current_side == 0:
                    self.name_tag_two.configure(bg='snow2', bd=1, highlightbackground='red', highlightthickness=1)
                    self.name_tag_two.place(x=350, y=50)
                    tkinter.Misc.lift(self.name_tag_two)

                    self.two_pl_canvas.place(x=350, y=100)
                    tkinter.Misc.lift(self.two_pl_canvas)

                    self.continue_button.place(x=350, y=310)
                    tkinter.Misc.lift(self.continue_button)
                elif self.current_side == 1:
                    self.name_tag_one.configure(bg='snow2', bd=1, highlightbackground='red', highlightthickness=1)
                    self.name_tag_one.place(x=350, y=50)
                    tkinter.Misc.lift(self.name_tag_one)

                    self.single_pl_canvas.place(x=350, y=100)
                    tkinter.Misc.lift(self.single_pl_canvas)

                    self.continue_button.place(x=350, y=310)
                    tkinter.Misc.lift(self.continue_button)
        sin_cos()

    def score_list(self):
        self.win_canvas.destroy()
        self.continue_button.destroy()
        self.single_pl_canvas.destroy()
        self.two_pl_canvas.destroy()
        self.name_tag_two.destroy()
        self.name_tag_one.destroy()
        self.lng_of_list = 0
        file = open('scores.txt', 'r')
        d = dict()
        for i in file:
            name, score = i.split()
            d[name] = float(score)

        if self.rslt == '=':
            if self.var.get() != 'Bot':
                if self.var.get() not in d:
                    d[self.var.get()] = 0.5
                else:
                    d[self.var.get()] += 0.5
            if self.entity != 'bot':
                if self.var_two.get() not in d:
                    d[self.var_two.get()] = 0.5
                else:
                    d[self.var_two.get()] += 0.5
        elif self.current_side == 0:
            if self.entity != 'bot':
                if self.var_two.get() not in d:
                    d[self.var_two.get()] = 1.0
                else:
                    d[self.var_two.get()] += 1.0
        elif self.current_side == 1:
            if self.var.get() != 'Bot':
                if self.var.get() not in d:
                    d[self.var.get()] = 1.0
                else:
                    d[self.var.get()] += 1.0
        if 'Anime' in d:
            pygame.mixer.init()
            pygame.mixer.music.load('anime_sound.ogg')
            pygame.mixer.music.play()
            del d['Anime']
            if 'Bot' in d:
                d['Bot'] += 0.001
            else:
                d['Bot'] = 0.001
        sorted_d = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
        file.close()
        file = open('scores.txt', 'w')
        for j in sorted_d:
            file.write('{} {}\n'.format(j[0], j[1]))
        file.close()
        self.main_screen()

    def only_list_of_scores(self, mode='notfrommenu'):
        file = open('scores.txt', 'r')
        for fl in file:
            self.lng_of_list += 1
        file.close()
        self.y_line = 65
        self.only_list_scores = tkinter.Canvas(width=900, height=400, highlightthickness=0, bg='#fffdd0')
        self.only_list_scores.pack()
        self.col_line = 85
        self.only_list_scores.create_line(200, self.y_line, 700, self.y_line, fill='black', width=3)
        self.only_list_scores.create_line(300, self.y_line - 40, 300, self.y_line, fill='black', width=3)
        self.only_list_scores.create_line(600, self.y_line - 40, 600, self.y_line, fill='black', width=3)
        self.only_list_scores.create_text(245, self.y_line - 20, text='#', font=self.font_in_game, fill='firebrick3')
        self.only_list_scores.create_text(450, self.y_line - 20, text='Name', font=self.font_in_game, fill='firebrick3')
        self.only_list_scores.create_text(650, self.y_line - 20, text='Score', font=self.font_in_game, fill='firebrick3')
        if self.lng_of_list < 1:
            self.only_list_scores.create_text(450, 85, text='No data', fill='gray', font=self.font_name)

        if self.lng_of_list > 7:
            self.lng_of_list = 8

        for n in range(self.lng_of_list-1):
            self.only_list_scores.create_line(200, self.y_line + 40, 700, self.y_line + 40, fill='black', width=3)
            self.only_list_scores.create_line(300, self.y_line - 40, 300, self.y_line, fill='black', width=3)
            self.only_list_scores.create_line(600, self.y_line - 40, 600, self.y_line, fill='black', width=3)
            self.y_line += 40
        if self.lng_of_list > 0:
            self.only_list_scores.create_line(300, self.y_line - 40, 300, self.y_line, fill='black', width=3)
            self.only_list_scores.create_line(600, self.y_line - 40, 600, self.y_line, fill='black', width=3)
            self.only_list_scores.create_line(300, self.y_line, 300, self.y_line + 40, fill='black', width=3)
            self.only_list_scores.create_line(600, self.y_line, 600, self.y_line + 40, fill='black', width=3)

        if mode != 'notfrommenu':
            self.bck_buttn('score')
            rst_button_image = tkinter.PhotoImage(file='img/reset_the_scores.png')
            rst_button = tkinter.Button(command=self.rst_results, image=rst_button_image, bd=0, bg='#fffdd0',
                                        activebackground='#fffdd0')
            rst_button.photo = rst_button_image
            self.only_list_scores.create_window(730 + 92, 358.43, window=rst_button)
        file = open('scores.txt', 'r')
        self.counttt = 1
        for nn in file:
            if self.counttt > 8:
                break
            name, score = nn.split()
            self.only_list_scores.create_text(245, self.col_line, text=self.counttt, fill='firebrick4', font=self.font_name)
            self.only_list_scores.create_text(450, self.col_line, text=name, fill='firebrick4', font=self.font_name)
            self.only_list_scores.create_text(650, self.col_line, text=score, fill='firebrick4', font=self.font_name)
            self.counttt += 1
            self.col_line += 40
        file.close()

    def rst_results(self):
        self.dest_score()
        file = open('scores.txt', 'w')
        file.close()
        self.lng_of_list = 0
        self.only_list_of_scores('from')

    def start_game(self, mode='one'):
        self.wwoonn = 0
        self.rslt = '-'
        self.side = random.randint(0, 1)
        self.current_side = self.side
        self.current = 1
        self.current_results = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight']
        self.nums = 3
        self.turn = 0
        self.single_pl_canvas.place(x=10, y=100)
        self.name_tag_func(10, 50, 'one')
        if mode == 'one':
            self.usr_ava(690, 100, 'two')
            self.name_tag_func(690, 50, 'bot')
            self.entity = 'bot'
        else:
            self.entity = 'human'
            self.name_tag_func(690, 50, 'two')
            self.two_pl_canvas.place(x=690, y=100)
        self.main_grid_func(262, 12)
        self.chosing_first_turn()
        root.after(3750, self.your_turn_label)
        root.after(3750, self.pick)


root = tkinter.Tk()
root.geometry('900x400+500+300')
root.title('Kappa')
root.resizable(False, False)
root.configure(background='#fffdd0')
root.iconbitmap('img/favicon.ico')
mr = MainReason(root)
root.mainloop()
