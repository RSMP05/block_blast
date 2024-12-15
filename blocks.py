def increment_grid_cell(grid, x, y):
    grid[y][x] += 1
    if grid[y][x] > 4:
        grid[y][x] = 0

def add_block(grid, block_parts, color):
    for part in block_parts:
        if part[0] < 0 or part[0] >= 8 or part[1] < 0 or part[1] >= 8:
            print("Out of bounds")
            return 0
        elif grid[part[0]][part[1]] != 0:
            print("No space")
            return 0
    for part in block_parts:
    	grid[part[0]][part[1]] = color

def initialise(x, y):
	global up_t
	up_t = [(y, x), (y, x+1), (y, x+2), (y+1, x+1)]

	global down_t
	down_t = [(y+1, x), (y+1, x+1), (y+1, x+2), (y, x+1)]

	global left_t
	left_t = [(y, x), (y+1, x), (y+1, x+1), (y+2, x)]

	global right_t
	right_t = [(y, x+1), (y+1, x+1), (y+1, x), (y+2, x+1)]

	global up_l_short_l
	up_l_short_l = [(y, x), (y, x+1), (y+1, x+1), (y+2, x+1)]

	global up_r_short_l
	up_r_short_l = [(y, x+1), (y, x), (y+1, x), (y+2, x)]

	global down_l_short_l
	down_l_short_l = [(y, x+1), (y+1, x+1), (y+2, x), (y+2, x+1)]

	global down_r_short_l
	down_r_short_l = [(y, x), (y+1, x), (y+2, x), (y+2, x+1)]

	global left_u_short_l
	left_u_short_l = [(y, x), (y+1, x), (y+1, x+1), (y+1, x+2)]

	global left_d_short_l
	left_d_short_l = [(y+1, x), (y, x), (y, x+1), (y, x+2)]

	global right_u_short_l
	right_u_short_l = [(y+1, x), (y+1, x+1), (y+1, x+2), (y, x+2)]

	global right_d_short_l
	right_d_short_l = [(y, x), (y, x+1), (y, x+2), (y+1, x+2)]

	global up_big_l
	up_big_l = [(y, x), (y, x+1), (y, x+2), (y+1, x+2), (y+2, x+2)]

	global down_big_l
	down_big_l = [(y+2, x), (y+1, x), (y, x), (y, x+1), (y, x+2)]

	global left_big_l
	left_big_l = [(y, x), (y+1, x), (y+2, x), (y+2, x+1), (y+2, x+2)]

	global right_big_l
	right_big_l = [(y, x+2), (y+1, x+2), (y+2, x+2), (y+2, x+1), (y+2, x)]

	global square
	square = [(y, x), (y, x+1), (y+1, x), (y+1, x+1)]

	global square_3x3
	square_3x3 = [(y, x), (y, x+1), (y, x+2), (y+1, x), (y+1, x+1), (y+1, x+2), (y+2, x), (y+2, x+1), (y+2, x+2)]

	global dot
	dot = [(y, x)]

	global line_1x2_h
	line_1x2_h = [(y, x), (y, x+1)]

	global line_1x2_v
	line_1x2_v = [(y, x), (y+1, x)]

	global line_1x3_h
	line_1x3_h = [(y, x), (y, x+1), (y, x+2)]

	global line_1x3_v
	line_1x3_v = [(y, x), (y+1, x), (y+2, x)]

	global line_1x4_h
	line_1x4_h = [(y, x), (y, x+1), (y, x+2), (y, x+3)]

	global line_1x4_v
	line_1x4_v = [(y, x), (y+1, x), (y+2, x), (y+3, x)]

	global line_1x5_h
	line_1x5_h = [(y, x), (y, x+1), (y, x+2), (y, x+3), (y, x+4)]

	global line_1x5_v
	line_1x5_v = [(y, x), (y+1, x), (y+2, x), (y+3, x), (y+4, x)]

	global rectangle_2x3_h
	rectangle_2x3_h = [(y, x), (y, x+1), (y, x+2), (y+1, x), (y+1, x+1), (y+1, x+2)]

	global rectangle_2x3_v
	rectangle_2x3_v = [(y, x), (y+1, x), (y+2, x), (y, x+1), (y+1, x+1), (y+2, x+1)]

	global s_piece
	s_piece = [(y, x), (y+1, x), (y+1, x+1), (y+2, x+1)]

	global s_piece_90
	s_piece_90 = [(y+2, x), (y+1, x), (y+1, x+1), (y, x+1)]

	global s_piece_180
	s_piece_180 = [(y+2, x+1), (y+1, x+1), (y+1, x), (y, x)]

	global s_piece_270
	s_piece_270 = [(y, x+1), (y+1, x+1), (y+1, x), (y+2, x)]

	global s_piece_flipped_h
	s_piece_flipped_h = [(y, x+1), (y+1, x+1), (y+1, x), (y+2, x)]

	global s_piece_flipped_v
	s_piece_flipped_v = [(y, x), (y+1, x), (y+1, x+1), (y+2, x+1)]

	global s_piece_horiz
	s_piece_horiz = [(y, x), (y, x+1), (y+1, x+1), (y+1, x+2)]

	global s_piece_90_horiz
	s_piece_90_horiz = [(y, x+2), (y+1, x+2), (y+1, x+1), (y+2, x+1)]

	global s_piece_180_horiz
	s_piece_180_horiz = [(y+1, x+2), (y+1, x+1), (y, x+1), (y, x+2)]

	global s_piece_270_horiz
	s_piece_270_horiz = [(y+2, x+1), (y+1, x+1), (y+1, x+2), (y, x+2)]

	global s_piece_flipped_horiz_h
	s_piece_flipped_horiz_h = [(y+1, x+2), (y+1, x+1), (y, x+1), (y, x+2)]

	global s_piece_flipped_horiz_v
	s_piece_flipped_horiz_v = [(y+1, x), (y, x), (y, x+1), (y, x+2)]

	global arr
	arr = [
	    up_t, down_t, left_t, right_t, up_l_short_l, up_r_short_l, down_l_short_l, down_r_short_l,
	    left_u_short_l, left_d_short_l, right_u_short_l, right_d_short_l, up_big_l, down_big_l, 
	    left_big_l, right_big_l, square, square_3x3, dot, line_1x2_h, line_1x2_v, line_1x3_h, 
	    line_1x3_v, line_1x4_h, line_1x4_v, line_1x5_h, line_1x5_v, rectangle_2x3_h, rectangle_2x3_v, s_piece, s_piece_90, 
	    s_piece_180, s_piece_270, s_piece_flipped_h, s_piece_flipped_v, s_piece_horiz, s_piece_90_horiz, 
	    s_piece_180_horiz, s_piece_270_horiz, s_piece_flipped_horiz_h, s_piece_flipped_horiz_v
	]

