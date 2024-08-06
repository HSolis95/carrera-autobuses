import platform

if platform.system() == 'Windows':
    import curses
else:
    import curses

def draw_buses(screen, positions, finish_line):
    screen.clear()
    height, width = screen.getmaxyx()
    bus1, bus2 = positions
    for i in range(height):
        screen.addch(i, finish_line, '|')
    screen.addstr(5, bus1, 'Bus 1')
    screen.addstr(7, bus2, 'Bus 2')
    screen.refresh()

def main(screen):
    curses.curs_set(0)
    screen.nodelay(1)
    screen.timeout(100)

    positions = [0, 0]
    finish_line = 50
    while True:
        draw_buses(screen, positions, finish_line)
        
        key = screen.getch()
        if key == ord('a'):
            positions[0] += 1
        elif key == ord('l'):
            positions[1] += 1
        
        if positions[0] >= finish_line or positions[1] >= finish_line:
            break

    screen.clear()
    if positions[0] >= finish_line:
        screen.addstr(10, 10, 'Bus 1 wins!')
    else:
        screen.addstr(10, 10, 'Bus 2 wins!')
    screen.refresh()
    screen.getch()

curses.wrapper(main)
