CC = g++
CFLAGS = -Wall -g
LDFLAGS = -lm

math.o : math.cpp math.h
	${CC} ${CFLAGS} -c math.cpp

test.o : test.cpp math.h
	${CC} ${CFLAGS} -c test.cpp

myprogram : test.o math.o
	${CC} ${CFLAGS} math.o test.o ${LDFLAGS} -o myprogram