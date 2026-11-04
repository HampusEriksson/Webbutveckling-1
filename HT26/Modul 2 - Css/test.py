import math
import random
import sys

import pygame


WIDTH = 1500
HEIGHT = 1200
FPS = 60
SEGMENT_COUNT = 10
SEGMENT_ANGLE = 360 / SEGMENT_COUNT
WHEEL_CENTER = (WIDTH // 2, 315)
WHEEL_RADIUS = 220

BACKGROUND = (18, 30, 37)
TEXT = (239, 245, 241)
MUTED = (163, 184, 181)
ACCENT = (218, 181, 97)
SEGMENT_COLORS = [
	(21, 123, 125),
	(26, 88, 103),
	(43, 139, 103),
	(33, 103, 121),
	(72, 139, 98),
	(29, 112, 112),
	(49, 101, 119),
	(35, 133, 111),
	(63, 117, 94),
	(32, 94, 111),
]


def number_for_segment(segment_index):
	return str(segment_index + 1)


def angle_for_number(number):
	segment_index = (int(number) - 1) % SEGMENT_COUNT
	segment_center = -90 + (segment_index + 0.5) * SEGMENT_ANGLE
	return (-90 - segment_center) % 360


def point_on_circle(center, radius, angle_degrees):
	angle = math.radians(angle_degrees)
	return (
		center[0] + math.cos(angle) * radius,
		center[1] + math.sin(angle) * radius,
	)


def draw_wheel(surface, rotation, fonts):
	center_x, center_y = WHEEL_CENTER

	pygame.draw.circle(surface, (9, 17, 22), WHEEL_CENTER, WHEEL_RADIUS + 12)
	pygame.draw.circle(surface, ACCENT, WHEEL_CENTER, WHEEL_RADIUS + 8, 3)

	for segment_index in range(SEGMENT_COUNT):
		start_angle = -90 + segment_index * SEGMENT_ANGLE + rotation
		end_angle = start_angle + SEGMENT_ANGLE
		arc_points = [
			point_on_circle(WHEEL_CENTER, WHEEL_RADIUS, start_angle + step * SEGMENT_ANGLE / 12)
			for step in range(13)
		]
		pygame.draw.polygon(
			surface,
			SEGMENT_COLORS[segment_index],
			[WHEEL_CENTER, *arc_points],
		)
		pygame.draw.lines(surface, (211, 190, 133), True, [WHEEL_CENTER, *arc_points], 2)

		middle_angle = start_angle + SEGMENT_ANGLE / 2
		label_position = point_on_circle(WHEEL_CENTER, WHEEL_RADIUS * 0.68, middle_angle)
		label = fonts["number"].render(number_for_segment(segment_index), True, TEXT)
		label_rect = label.get_rect(center=label_position)
		surface.blit(label, label_rect)

	pygame.draw.circle(surface, ACCENT, WHEEL_CENTER, 31)
	pygame.draw.circle(surface, (237, 242, 230), WHEEL_CENTER, 25)
	pygame.draw.circle(surface, (28, 45, 52), WHEEL_CENTER, 12)

	pointer_points = [
		(center_x, center_y - WHEEL_RADIUS + 3),
		(center_x - 19, center_y - WHEEL_RADIUS - 30),
		(center_x + 19, center_y - WHEEL_RADIUS - 30),
	]
	pygame.draw.polygon(surface, ACCENT, pointer_points)
	pygame.draw.polygon(surface, TEXT, pointer_points, 2)


def draw_result_panel(surface, spinning, result_number, fonts):
	panel = pygame.Rect(WIDTH // 2 - 145, 570, 290, 100)
	pygame.draw.rect(surface, (25, 42, 43), panel, border_radius=8)
	pygame.draw.rect(surface, (114, 96, 61), panel, width=2, border_radius=8)

	if spinning:
		label = fonts["result_label"].render("DRAGNING PÅGÅR", True, ACCENT)
		surface.blit(label, label.get_rect(center=(WIDTH // 2, panel.centery)))
	else:
		label_text = "VINNANDE NUMMER" if result_number is not None else "NÄSTA DRAGNING"
		label = fonts["result_label"].render(label_text, True, MUTED)
		surface.blit(label, label.get_rect(center=(WIDTH // 2, panel.y + 28)))
		value = result_number if result_number is not None else "-"
		number = fonts["result_number"].render(value, True, ACCENT)
		surface.blit(number, number.get_rect(center=(WIDTH // 2, panel.y + 69)))


def main():
	pygame.init()
	pygame.display.set_caption("Sifferlotteriet")
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	clock = pygame.time.Clock()

	fonts = {
		"title": pygame.font.Font(None, 48),
		"number": pygame.font.Font(None, 34),
		"result_label": pygame.font.Font(None, 21),
		"result_number": pygame.font.Font(None, 43),
	}

	number_keys = {
		pygame.K_0: "10",
		pygame.K_1: "1",
		pygame.K_2: "2",
		pygame.K_3: "3",
		pygame.K_4: "4",
		pygame.K_5: "5",
		pygame.K_6: "6",
		pygame.K_7: "7",
		pygame.K_8: "8",
		pygame.K_9: "9",
	}

	selected_number = None
	rotation = 0.0
	spin_start = 0.0
	spin_end = 0.0
	spin_started_at = 0
	spin_duration = 7000
	spinning = False
	result_number = None
	running = True

	while running:
		now = pygame.time.get_ticks()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.KEYDOWN and not spinning and event.key in number_keys:
				selected_number = number_keys[event.key]
				result_number = None
				spin_start = rotation
				landing_offset = random.uniform(-SEGMENT_ANGLE * 0.42, SEGMENT_ANGLE * 0.42)
				final_angle = (angle_for_number(selected_number) + landing_offset) % 360
				extra_turns = random.randint(8, 11) * 360
				forward_distance = (final_angle - (spin_start % 360)) % 360
				spin_end = spin_start + extra_turns + forward_distance
				spin_started_at = now
				spinning = True

		if spinning:
			progress = min((now - spin_started_at) / spin_duration, 1.0)
			eased_progress = 1 - (1 - progress) ** 4
			rotation = spin_start + (spin_end - spin_start) * eased_progress
			if progress >= 1:
				rotation = spin_end
				spinning = False
				result_number = selected_number
				rotation %= 360

		screen.fill(BACKGROUND)

		title = fonts["title"].render("LOTTERI", True, TEXT)
		screen.blit(title, title.get_rect(center=(WIDTH // 2, 43)))

		draw_wheel(screen, rotation, fonts)
		draw_result_panel(screen, spinning, result_number, fonts)

		pygame.display.flip()
		clock.tick(FPS)

	pygame.quit()
	sys.exit()


if __name__ == "__main__":
	main()
