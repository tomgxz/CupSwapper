from manim import *

paths=["CA","BA","BC","CB","AB","CB","AC","CB","CA","BA","BA","CA","CB","AB"]

class CupSwapperScene(Scene):
    def construct(self):
        cupA=Circle();cupB=Circle();cupC=Circle();
        cupA.set_color(WHITE)
        cupB.set_color(WHITE)
        cupC.set_color(WHITE)

        cups=[cupA,cupB,cupC]
        selected=1
        oldselected=selected

        cupA.next_to(cupB,LEFT,buff=0.5)
        cupC.next_to(cupB,RIGHT,buff=0.5)

        titleText = MarkupText("Cup Swapper",font_size=64,color=WHITE)
        titleText.next_to(cupB,UP,buff=1.5)

        textA = MarkupText("Cup A",font_size=32,color=WHITE)
        textA.next_to(cupA,UP,buff=0.5)

        textB = MarkupText("Cup B",font_size=32,color=WHITE)
        textB.next_to(cupB,UP,buff=0.5)

        textC = MarkupText("Cup C",font_size=32,color=WHITE)
        textC.next_to(cupC,UP,buff=0.5)

        self.play( Create(titleText) )

        self.play( Create(textA),Create(textB),Create(textC) )

        self.play( Create(cupA), run_time=0.5)

        self.play( Create(cupB), run_time=0.5)

        self.play( Create(cupC), run_time=0.5)

        self.play(
            cupA.animate.set_fill(GRAY,opacity=1),
            cupB.animate.set_fill(WHITE,opacity=1),
            cupC.animate.set_fill(GRAY,opacity=1),
        )

        compare=["a","b","c"]

        circleMoveRuntime=0.5

        for path in paths:
            move=list(path.lower())

            pos1=compare.index(move[0])
            pos2=compare.index(move[1])

            oldselected=selected

            playBaseAni=True

            if 0 not in [pos1,pos2]:
                if selected==1: selected=2
                elif selected==2: selected=1

                if selected == 0:
                    self.play(
                        cups[1].animate.next_to(cups[1],RIGHT,buff=0.5),
                        cups[2].animate.next_to(cups[2],LEFT,buff=0.5),
                        run_time=circleMoveRuntime
                    )
                    playBaseAni=False


            elif 1 not in [pos1,pos2]:
                if selected==0: selected=2
                elif selected==2: selected=0

                if selected == 1:
                    self.play(
                        cups[0].animate.next_to(cups[1],RIGHT,buff=0.5),
                        cups[2].animate.next_to(cups[1],LEFT,buff=0.5),
                        run_time=circleMoveRuntime
                    )
                    playBaseAni=False
            elif 2 not in [pos1,pos2]:
                if selected==1: selected=0
                elif selected==0: selected=1

                if selected == 2:
                    self.play(
                        cups[1].animate.next_to(cups[1],LEFT,buff=0.5),
                        cups[0].animate.next_to(cups[0],RIGHT,buff=0.5),
                        run_time=circleMoveRuntime
                    )
                    playBaseAni=False

            if playBaseAni:
                self.play(
                    cups[oldselected].animate.next_to(cups[selected+1],LEFT,buff=0.5) if selected < 2 else cups[oldselected].animate.next_to(cups[selected-1],RIGHT,buff=0.5),

                    cups[selected].animate.next_to(cups[oldselected+1],LEFT,buff=0.5) if oldselected < 2 else cups[selected].animate.next_to(cups[oldselected-1],RIGHT,buff=0.5),

                    run_time=circleMoveRuntime
                )

            if 0 not in [pos1,pos2]: cups = [ cups[0],cups[2],cups[1] ]
            elif 1 not in [pos1,pos2]: cups = [ cups[2],cups[1],cups[0] ]
            elif 2 not in [pos1,pos2]: cups = [ cups[1],cups[0],cups[2] ]

        self.wait(1)

        if selected==0: self.play( FadeOut(cups[1],cups[2]),textA.animate.set_color(GREEN) )
        if selected==1: self.play( FadeOut(cups[0],cups[2]),textB.animate.set_color(GREEN) )
        if selected==2: self.play( FadeOut(cups[0],cups[1]),textC.animate.set_color(GREEN) )

        self.wait(1)

# python -m manim -pql scene.py CupSwapperScene
