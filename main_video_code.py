from manim import *

class TeamIntro(Scene):
    def construct(self):

        # --- Step 1: Title ---
        text_1 = Text("The", font="Pirata One", fill_color="#FFD43F", font_size=80)
        text_2 = Text("Pythons", font="Pirata One", fill_color="#2A456C", font_size=80)
        title_group = VGroup(text_1, text_2).arrange(RIGHT, buff=0.2)
        text_2.shift(DOWN * 0.1)
        self.play(Write(title_group), run_time=0.6)

        box = SurroundingRectangle(title_group, color=WHITE, buff=0.3)
        self.play(Create(box), runtime=0.6)

        logo_group = VGroup(box, title_group)
        self.play(logo_group.animate.scale(1.1), run_time=3)
        self.play(FadeOut(logo_group))

        # --- Step 2: Transition text ---
        next_text = Text("Meet the minds behind the machine", font_size=50, color=WHITE)
        self.play(Write(next_text), run_time=1)
        self.wait(0.2)
        self.play(FadeOut(next_text))

        # --- Step 3: Team Members ---
        team_members = [
            {"name": "Ahmed Ishiba", "role": "Software Lead", "photo": "sayed.png"},
            {"name": "Eyad Nazary", "role": "Electrical Lead", "photo": "eyad.png"},
            {"name": "Nour Eldin Raoof", "role": "Mechanical Lead", "photo": "nour.png"},
        ]

        member_groups = []
        for member in team_members:
            photo = ImageMobject(member["photo"]).scale(0.6)
            name_text = Text(member["name"], font_size=36, color=WHITE)
            role_text = Text(member["role"], font_size=28, color=GRAY)
            group = Group(photo, name_text, role_text).arrange(DOWN, buff=0.15)
            member_groups.append(group)

        all_members = Group(*member_groups).arrange(RIGHT, buff=1.2).move_to(ORIGIN)
        self.play(FadeIn(all_members, shift=UP), run_time=1)
        self.wait(2.6)
        self.play(FadeOut(all_members))
        ######################################################
        achievments_text = Text("Dominating the Egypt Qualifier!", font_size=52, color=WHITE).to_edge(UP)
        self.play(Write(achievments_text), run_time=1)
        text_achievements = Text("•1st place Egypt Qualifier 2025\nqualified for international finals in Singapore 26-28 November\nrepresenting Egypt", font_size=36, color=WHITE, line_spacing=1.5).next_to(achievments_text, DOWN, buff=0.5).to_edge(LEFT, buff=0.2)
        self.play(Write(text_achievements), run_time=1)
        self.wait(1.5)
        self.play(FadeOut(achievments_text),FadeOut(text_achievements))

        ######################################################
        # --- Step 4: Competition Intro ---
        competition_text = Text("World Robot Olympiad 2025", font_size=52, color=WHITE)
        competition_text.to_edge(UP)
        self.play(Write(competition_text), run_time=1)

        # --- WRO Logo below the title ---
        wro_logo = ImageMobject("WRO_logo-removebg.png").scale(1).next_to(competition_text, DOWN, buff=0.5)
        self.play(FadeIn(wro_logo), run_time=1)

        # --- Section Title ---
        text_3 = Text("Competition Goal", font_size=40, color=WHITE).next_to(wro_logo, DOWN, buff=0.5, aligned_edge=LEFT)
        self.play(Write(text_3), run_time=1)

        # --- Bullet Points ---
        goals = [
            "• Cultivate a generation of young self-driving car engineers",
            "• Design and build an autonomous self-driving car",
            "• Evade traffic signs according to their color",
        ]

        bullet_texts = VGroup(*[
            Text(goal, font_size=30, color=WHITE)
            for goal in goals
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(text_3, DOWN, buff=0.4)

        # --- Additional Info ---
        text_4 = Text(
            "Competition is divided into open challenge and obstacle challenge",
            font_size=34, color=WHITE
        ).next_to(bullet_texts, DOWN, buff=0.6)

        # --- Combine all text elements ---
        content_group = VGroup(bullet_texts, text_4)
        content_group.to_edge(LEFT, buff=1.2)

        # --- Animate Content ---
        self.play(Write(bullet_texts), run_time=2)
        self.play(Write(text_4), run_time=1.5)

        # --- Wait and Fade Out ---
        self.wait(3)
        self.play(FadeOut(text_3),FadeOut(content_group), FadeOut(competition_text), FadeOut(wro_logo))
              # --- Step 5: Challenges Section ---
        track = ImageMobject("track.png").scale(0.65)
        track.to_edge(UP, buff=0.5)
        self.play(FadeIn(track), run_time=1)

        # Bullet points explaining the challenges
        open_challenge = Text(
            "• In the open challenge, the robot must complete 3 laps on this track\n  while following lines accurately.",
            font_size=26, color=WHITE, line_spacing=1.2,
        ).to_edge(LEFT).next_to(track, DOWN, buff=0.6)

        obstacle_challenge = Text(
            "• In the obstacle challenge, the robot must complete 3 laps while\n  avoiding red and green traffic signs.",
            font_size=26, color=WHITE, line_spacing=1.2,
        ).to_edge(LEFT).next_to(open_challenge, DOWN, buff=0.4).shift(LEFT * 0.3)

        # Show text after image appears
        self.play(Write(open_challenge), run_time=1)
        self.wait(0.5)
        self.play(Write(obstacle_challenge), run_time=1)
        self.wait(3)
        self.play(FadeOut(track), FadeOut(open_challenge), FadeOut(obstacle_challenge))
        
        display_robot_text = Text("The minds behind the machine..\nnow meet the machine itself!", font_size=52, color=WHITE)
        self.play(Write(display_robot_text), run_time=1)
        self.wait(0.6)
        self.play(FadeOut(display_robot_text))
        ######################################################
        
        components = [
            {"pos": RIGHT * 0.3 + DOWN * 0.3, "color": "#FFD43F", "label": "KB2040", "radius": 0.6, "specs":"•Responsible\nfor motor conrol"}, 
            {"pos": RIGHT * 1.3 + DOWN * 1, "color": "#FFD43F", "label": "Arducam", "radius": 0.6, "specs":"• 180 degree FOV\nto detect traffic signs\nanywhere"},
            {"pos": RIGHT * 4 + UP * 1, "color": "#FFD43F", "label": "Raspberry Pi 5", "radius": 0.6, "specs":"• 8GB RAM, 5 GHz\n• main computer processing\nall sensor data and running\nML models"},
            {"pos": RIGHT * 5 + UP * 0.3, "color": "#FFD43F", "label": "Coral Accelerator", "radius": 0.6, "specs":"• External TPU for running ML models\nfaster and more efficiently"},
            {"pos": DOWN * 1.7 + RIGHT * 2.7, "color": "#FFD43F", "label": "MPU6050", "radius": 0.6, "specs":"•measure orientation\nand rotation degrees"},
            {"pos": DOWN * 1.5 + RIGHT * 3.5, "color": "#FFD43F", "label": "Ultrasonic Sensor", "radius": 0.6, "specs":"•measure distance from walls \nand fuse with camera data\nto map surroundings"},
            {"pos": RIGHT + DOWN * 1.7, "color": "#FFD43F", "label": "TOF Sensor", "radius": 0.6, "specs":"•Time Of Flight\nsensor\n•get distance from\nparking lot walls\n"},
        ]

        robot_image = ImageMobject("iso_view.jpeg").scale(0.3)
        self.play(FadeIn(robot_image), run_time=1)
        self.play(robot_image.animate.to_edge(RIGHT), run_time=1)

        # Draw for components on the RIGHT side
        for component in components:
            circle = Circle(
                radius=component["radius"],
                color=component["color"],
                stroke_width=8
            ).move_to(component["pos"])

            # --- Create sharp-bent arrow path ---
            start_point = circle.get_left()
            bend_point = start_point + LEFT * 0.5  # small horizontal move
            end_point = bend_point + UP * (0.5 if component["pos"][1] > 0 else -0.5) + LEFT * 1.5

            # Combine lines
            arrow_path = VGroup(
                Line(start_point, bend_point, color=component["color"], stroke_width=8),
                Line(bend_point, end_point, color=component["color"], stroke_width=8),
                Arrow(end_point, end_point + LEFT * 2, color=component["color"], buff=0, stroke_width=8).scale(1)
            )
            # Label near the arrow end
            label = Text(component["label"], font_size=40, color="#2A456C", weight=BOLD)
            specs = Text(component["specs"], font_size=25,weight=BOLD, color=WHITE,stroke_color=BLACK, stroke_width=1).next_to(label, DOWN)
            component_info = VGroup(label, specs).arrange(DOWN, aligned_edge=LEFT).next_to(arrow_path[-1], LEFT)
            self.play(Create(arrow_path), Write(component_info),Create(circle), run_time=0.7)
            self.wait(1.7)
            self.play(FadeOut(arrow_path),FadeOut(component_info),FadeOut(circle), run_time=0.5)
        ######################################################
        self.play(FadeOut(robot_image))

        mechanical_text = Text("A healthy mind in a healthy body!\nlet's start with our mechancial design", font_size=48, color=WHITE).to_edge(UP)
        solid_photo = ImageMobject("robot_solid.jpeg").scale(2).next_to(mechanical_text, DOWN, buff=0.5)
        buzzwords = Text("•Servo-actuated front-wheel steering\n•Lightweight modular chassis ensures stability\n   and serviceability\n•CAD-driven design", font_size=30, color=WHITE, line_spacing=1.3).next_to(mechanical_text, DOWN, buff=0.5).to_edge(LEFT)
        self.play(Write(mechanical_text), run_time=1)
        self.play(Write(buzzwords), run_time=0.6)
        self.wait(10)
        self.play(FadeOut(mechanical_text),FadeOut(buzzwords))
        ######################################################
        electrical_text = Text("Powering the python!", font_size=48, color=WHITE).to_edge(UP)
        pcb_photo = ImageMobject("fusion_pcb.png").scale(0.7).next_to(electrical_text, DOWN, buff=0.5)
        pcb_buzzwords = Text("•Designed and implemented from A to Z by us\n•integrate all sensors and actuators\n•Ensures reliable connections\n and efficient power distribution\n•Our body is the design itself!\n•Double-layer PCB design\n that enhances compactness and reliablity\n for a fault-proof system", font_size=30, color=WHITE, line_spacing=1.3).next_to(electrical_text, DOWN, buff=0.5).to_edge(LEFT)
        self.play(Write(electrical_text), run_time=1)
        self.play(Write(pcb_buzzwords), run_time=0.6)
        self.wait(10)
        self.play(FadeOut(electrical_text),FadeOut(pcb_buzzwords))
        ######################################################
        software_text = Text("We built the body and wired the nerves\nnow it's time for the brain", font_size=48, color=WHITE).to_edge(UP)
        code_photo = ImageMobject("detection.png").scale(0.5).next_to(software_text, DOWN, buff=0.5)
        code_buzzwords = Text("•Computer vision algorithms for frame-by-frame\n  analysis\n•Sensor fusion technique for accurate navigation\n•Real-time decision making for obstacle\n  avoidance\n•Custom trained AI model with over 700 photos\nfor accurate detection and decision-making\n•Accelerated with Google Coral Accelerator Edge TPU for high speed detection", font_size=30, color=WHITE, line_spacing=1.3).next_to(software_text, DOWN, buff=0.5).to_edge(LEFT)
        self.play(Write(software_text), run_time=1)
        self.wait(0.2)
        self.play(FadeIn(code_photo), run_time=1)
        self.play(code_photo.animate.to_edge(RIGHT), run_time=1)
        self.play(Write(code_buzzwords), run_time=0.6)
        self.wait(3.7)
        self.play(FadeOut(software_text),FadeOut(code_photo),FadeOut(code_buzzwords))
        ###################################################### 
        video_text = Text("Enough talk — time for some action!", font_size=52, color=WHITE, weight=BOLD)
        self.play(Write(video_text), run_time=0.9)
        self.wait(0.3)
        self.play(FadeOut(video_text))
        self.wait(18)  # Pause for video duration
        ######################################################
        funding_text = Text("The Pythons are heading to the World Stage — with your support!", font_size=30, color=WHITE).shift(UP * 1.5)
        funding_text2 = Text("Every contribution brings us one step closer to representing Egypt on the global stage.", font_size=30, color=WHITE).next_to(funding_text, DOWN, buff=0.5)
        self.play(Write(funding_text), run_time=1)
        self.play(Write(funding_text2), run_time=1)
        wro_final_logo = ImageMobject("WRO_Final.png").scale(0.5).next_to(funding_text2, DOWN, buff=0.7)
        date = Text("26-28 November 2025", font_size=30, color=WHITE).next_to(wro_final_logo, DOWN, buff=0.3)
        self.play(FadeIn(wro_final_logo), Write(date), run_time=1)
        self.wait(2)
        self.play(FadeOut(funding_text),FadeOut(funding_text2),FadeOut(wro_final_logo),FadeOut(date))
        ######################################################
        closing_text = Text("Thank you for your attention!", font_size=52, color=WHITE, weight=BOLD)
        self.play(Write(closing_text), run_time=1)
        text_1 = Text("The", font="Pirata One", fill_color="#FFD43F", font_size=80)
        text_2 = Text("Pythons", font="Pirata One", fill_color="#2A456C", font_size=80)
        title_group = VGroup(text_1, text_2).arrange(RIGHT, buff=0.2).next_to(closing_text, DOWN, buff=0.5)
        text_2.shift(DOWN * 0.1)
        self.play(Write(title_group), run_time=0.9)
        self.wait(3)

