# Makefile
#

SYS = apple2

CC = cc65
AS = ca65
LD = ld65
AR = ar65
CP = cp
RM = rm -f
MD = mkdir
CT2UTL = ct2utils

SDIR = src
ODIR = obj
LDIR = ../../apple2lib
IDIR = $(LDIR)/inc

CFLAGS  = -t $(SYS) -O -I$(IDIR) -I.
AFLAGS  = -t $(SYS) -l $(ODIR)/$(*).lst -I$(IDIR) -I.
LDFLAGS = -C $(LDIR)/_config


all: $(ODIR) ct2

OBJS1 = $(ODIR)/tk2k_ar.o
OBJS2 = $(ODIR)/pitfall2.o

tk2k_ar: $(OBJS1)
	$(LD) $(LDFLAGS) -o $@#060036 $^

pitfall2: $(OBJS2)
	$(LD) $(LDFLAGS) -o $@#0608FD $^

ct2: tk2k_ar pitfall2
	$(CT2UTL) pitfall2.ct2 -c
	$(CT2UTL) pitfall2.ct2 -i -f tk2k_ar#060036 -t PITFII
	$(CT2UTL) pitfall2.ct2 -i -f pitfall2#0608FD -t PITFII
	
$(ODIR):
	$(MD) $(ODIR)

clean:
	$(RM) $(ODIR)/* tk2k_ar#060036 pitfall2#0608FD

$(ODIR)/%.o: $(SDIR)/%.c
	$(CC) $(CFLAGS) -o $(ODIR)/$(*).a65 $<
	$(AS) $(AFLAGS) -o $@ $(ODIR)/$(*).a65

$(ODIR)/%.o: $(SDIR)/%.a65
	$(AS) $(AFLAGS) -o $@ $<
