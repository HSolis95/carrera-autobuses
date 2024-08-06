import platform
import sys
import os

if platform.system() == 'Windows':
    import curses
else:
    import curses

# Arte ASCII para el bus
bus_ascii = [
    "        ______________________",
    "       |,----.,----.,----.,--.\\",
    "       ||    ||    ||    ||   \\\\",
    "       |`----'`----'|----||----\\`.",
    "       [            |   -||- __|( |",
    "       [  ,--.      |____||.--.  |",
    "       =-(( `))-----------(( `))=="
]

def draw_buses(screen, positions, finish_line):
    screen.clear()
    height, width = screen.getmaxyx()
    bus1, bus2 = positions
    
    # Dibujar la línea de meta
    for i in range(height):
        screen.addch(i, finish_line, '|')
    
    # Dibujar los buses
    for i, line in enumerate(bus_ascii):
        screen.addstr(5 + i, bus1, line)
        screen.addstr(15 + i, bus2, line)
    
    screen.refresh()

def main(screen, test_mode=False):
    curses.curs_set(0)
    screen.nodelay(1)
    screen.timeout(100)

    positions = [0, 0]
    finish_line = 50

    if test_mode:
        # Simular una carrera rápida para pruebas
        positions = [finish_line - 1, finish_line - 2]

    while True:
        draw_buses(screen, positions, finish_line)
        
        if not test_mode:
            key = screen.getch()
            if key == ord('a'):
                positions[0] += 1
            elif key == ord('l'):
                positions[1] += 1
        else:
            # Simular presiones de teclas
            positions[0] += 1
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

if __name__ == "__main__":
    test_mode = '--test' in sys.argv or os.getenv('TEST_MODE') == 'true'
    curses.wrapper(lambda scr: main(scr, test_mode))
