	.section	__TEXT,__text,regular,pure_instructions
	.globl	__Z5sort3Pii
	.align	4, 0x90
__Z5sort3Pii:                           ## @_Z5sort3Pii
	.cfi_startproc
## BB#0:
	pushq	%rbp
Ltmp2:
	.cfi_def_cfa_offset 16
Ltmp3:
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
Ltmp4:
	.cfi_def_cfa_register %rbp
	movq	%rdi, -8(%rbp)
	movl	%esi, -12(%rbp)
	movq	-8(%rbp), %rdi
	movl	4(%rdi), %esi
	movq	-8(%rbp), %rdi
	cmpl	8(%rdi), %esi
	jle	LBB0_2
## BB#1:
	movq	-8(%rbp), %rax
	movl	4(%rax), %ecx
	movl	%ecx, -16(%rbp)
	movq	-8(%rbp), %rax
	movl	8(%rax), %ecx
	movq	-8(%rbp), %rax
	movl	%ecx, 4(%rax)
	movl	-16(%rbp), %ecx
	movq	-8(%rbp), %rax
	movl	%ecx, 8(%rax)
LBB0_2:
	movq	-8(%rbp), %rax
	movl	4(%rax), %ecx
	movq	-8(%rbp), %rax
	cmpl	12(%rax), %ecx
	jle	LBB0_4
## BB#3:
	movq	-8(%rbp), %rax
	movl	4(%rax), %ecx
	movl	%ecx, -16(%rbp)
	movq	-8(%rbp), %rax
	movl	12(%rax), %ecx
	movq	-8(%rbp), %rax
	movl	%ecx, 4(%rax)
	movl	-16(%rbp), %ecx
	movq	-8(%rbp), %rax
	movl	%ecx, 12(%rax)
LBB0_4:
	movq	-8(%rbp), %rax
	movl	8(%rax), %ecx
	movq	-8(%rbp), %rax
	cmpl	12(%rax), %ecx
	jle	LBB0_6
## BB#5:
	movq	-8(%rbp), %rax
	movl	8(%rax), %ecx
	movl	%ecx, -16(%rbp)
	movq	-8(%rbp), %rax
	movl	12(%rax), %ecx
	movq	-8(%rbp), %rax
	movl	%ecx, 8(%rax)
	movl	-16(%rbp), %ecx
	movq	-8(%rbp), %rax
	movl	%ecx, 12(%rax)
LBB0_6:
	popq	%rbp
	ret
	.cfi_endproc

	.globl	__Z14selection_sortPii
	.align	4, 0x90
__Z14selection_sortPii:                 ## @_Z14selection_sortPii
	.cfi_startproc
## BB#0:
	pushq	%rbp
Ltmp7:
	.cfi_def_cfa_offset 16
Ltmp8:
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
Ltmp9:
	.cfi_def_cfa_register %rbp
	movq	%rdi, -8(%rbp)
	movl	%esi, -12(%rbp)
	movl	$0, -16(%rbp)
LBB1_1:                                 ## =>This Loop Header: Depth=1
                                        ##     Child Loop BB1_3 Depth 2
	movl	-16(%rbp), %eax
	cmpl	-12(%rbp), %eax
	jge	LBB1_10
## BB#2:                                ##   in Loop: Header=BB1_1 Depth=1
	movl	-16(%rbp), %eax
	movl	%eax, -24(%rbp)
	movl	-16(%rbp), %eax
	movl	%eax, -20(%rbp)
LBB1_3:                                 ##   Parent Loop BB1_1 Depth=1
                                        ## =>  This Inner Loop Header: Depth=2
	movl	-20(%rbp), %eax
	cmpl	-12(%rbp), %eax
	jge	LBB1_8
## BB#4:                                ##   in Loop: Header=BB1_3 Depth=2
	movslq	-24(%rbp), %rax
	movq	-8(%rbp), %rcx
	movl	(%rcx,%rax,4), %edx
	movslq	-20(%rbp), %rax
	movq	-8(%rbp), %rcx
	cmpl	(%rcx,%rax,4), %edx
	jle	LBB1_6
## BB#5:                                ##   in Loop: Header=BB1_3 Depth=2
	movl	-20(%rbp), %eax
	movl	%eax, -24(%rbp)
LBB1_6:                                 ##   in Loop: Header=BB1_3 Depth=2
	jmp	LBB1_7
LBB1_7:                                 ##   in Loop: Header=BB1_3 Depth=2
	movl	-20(%rbp), %eax
	addl	$1, %eax
	movl	%eax, -20(%rbp)
	jmp	LBB1_3
LBB1_8:                                 ##   in Loop: Header=BB1_1 Depth=1
	movslq	-24(%rbp), %rax
	movq	-8(%rbp), %rcx
	movl	(%rcx,%rax,4), %edx
	movl	%edx, -28(%rbp)
	movslq	-16(%rbp), %rax
	movq	-8(%rbp), %rcx
	movl	(%rcx,%rax,4), %edx
	movslq	-24(%rbp), %rax
	movq	-8(%rbp), %rcx
	movl	%edx, (%rcx,%rax,4)
	movl	-28(%rbp), %edx
	movslq	-16(%rbp), %rax
	movq	-8(%rbp), %rcx
	movl	%edx, (%rcx,%rax,4)
## BB#9:                                ##   in Loop: Header=BB1_1 Depth=1
	movl	-16(%rbp), %eax
	addl	$1, %eax
	movl	%eax, -16(%rbp)
	jmp	LBB1_1
LBB1_10:
	popq	%rbp
	ret
	.cfi_endproc

	.globl	__Z14insertion_sortPii
	.align	4, 0x90
__Z14insertion_sortPii:                 ## @_Z14insertion_sortPii
	.cfi_startproc
## BB#0:
	pushq	%rbp
Ltmp12:
	.cfi_def_cfa_offset 16
Ltmp13:
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
Ltmp14:
	.cfi_def_cfa_register %rbp
	movq	%rdi, -8(%rbp)
	movl	%esi, -12(%rbp)
	movl	$1, -16(%rbp)
LBB2_1:                                 ## =>This Loop Header: Depth=1
                                        ##     Child Loop BB2_3 Depth 2
	movl	-16(%rbp), %eax
	cmpl	-12(%rbp), %eax
	jge	LBB2_9
## BB#2:                                ##   in Loop: Header=BB2_1 Depth=1
	movl	-16(%rbp), %eax
	movl	%eax, -20(%rbp)
	movslq	-16(%rbp), %rcx
	movq	-8(%rbp), %rdx
	movl	(%rdx,%rcx,4), %eax
	movl	%eax, -24(%rbp)
LBB2_3:                                 ##   Parent Loop BB2_1 Depth=1
                                        ## =>  This Inner Loop Header: Depth=2
	movb	$0, %al
	cmpl	$0, -20(%rbp)
	movb	%al, -25(%rbp)          ## 1-byte Spill
	jle	LBB2_5
## BB#4:                                ##   in Loop: Header=BB2_3 Depth=2
	movl	-20(%rbp), %eax
	subl	$1, %eax
	movslq	%eax, %rcx
	movq	-8(%rbp), %rdx
	movl	(%rdx,%rcx,4), %eax
	cmpl	-24(%rbp), %eax
	setg	%sil
	movb	%sil, -25(%rbp)         ## 1-byte Spill
LBB2_5:                                 ##   in Loop: Header=BB2_3 Depth=2
	movb	-25(%rbp), %al          ## 1-byte Reload
	testb	$1, %al
	jne	LBB2_6
	jmp	LBB2_7
LBB2_6:                                 ##   in Loop: Header=BB2_3 Depth=2
	movl	-20(%rbp), %eax
	subl	$1, %eax
	movslq	%eax, %rcx
	movq	-8(%rbp), %rdx
	movl	(%rdx,%rcx,4), %eax
	movslq	-20(%rbp), %rcx
	movq	-8(%rbp), %rdx
	movl	%eax, (%rdx,%rcx,4)
	movl	-20(%rbp), %eax
	addl	$4294967295, %eax       ## imm = 0xFFFFFFFF
	movl	%eax, -20(%rbp)
	jmp	LBB2_3
LBB2_7:                                 ##   in Loop: Header=BB2_1 Depth=1
	movl	-24(%rbp), %eax
	movslq	-20(%rbp), %rcx
	movq	-8(%rbp), %rdx
	movl	%eax, (%rdx,%rcx,4)
## BB#8:                                ##   in Loop: Header=BB2_1 Depth=1
	movl	-16(%rbp), %eax
	addl	$1, %eax
	movl	%eax, -16(%rbp)
	jmp	LBB2_1
LBB2_9:
	popq	%rbp
	ret
	.cfi_endproc

	.globl	__Z11bubble_sortPii
	.align	4, 0x90
__Z11bubble_sortPii:                    ## @_Z11bubble_sortPii
	.cfi_startproc
## BB#0:
	pushq	%rbp
Ltmp17:
	.cfi_def_cfa_offset 16
Ltmp18:
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
Ltmp19:
	.cfi_def_cfa_register %rbp
	movq	%rdi, -8(%rbp)
	movl	%esi, -12(%rbp)
	movl	-12(%rbp), %esi
	subl	$1, %esi
	movl	%esi, -16(%rbp)
LBB3_1:                                 ## =>This Loop Header: Depth=1
                                        ##     Child Loop BB3_3 Depth 2
	cmpl	$0, -16(%rbp)
	jl	LBB3_10
## BB#2:                                ##   in Loop: Header=BB3_1 Depth=1
	movl	$1, -20(%rbp)
LBB3_3:                                 ##   Parent Loop BB3_1 Depth=1
                                        ## =>  This Inner Loop Header: Depth=2
	movl	-20(%rbp), %eax
	cmpl	-16(%rbp), %eax
	jg	LBB3_8
## BB#4:                                ##   in Loop: Header=BB3_3 Depth=2
	movl	-20(%rbp), %eax
	subl	$1, %eax
	movslq	%eax, %rcx
	movq	-8(%rbp), %rdx
	movl	(%rdx,%rcx,4), %eax
	movslq	-20(%rbp), %rcx
	movq	-8(%rbp), %rdx
	cmpl	(%rdx,%rcx,4), %eax
	jle	LBB3_6
## BB#5:                                ##   in Loop: Header=BB3_3 Depth=2
	movl	-20(%rbp), %eax
	subl	$1, %eax
	movslq	%eax, %rcx
	movq	-8(%rbp), %rdx
	movl	(%rdx,%rcx,4), %eax
	movl	%eax, -24(%rbp)
	movslq	-20(%rbp), %rcx
	movq	-8(%rbp), %rdx
	movl	(%rdx,%rcx,4), %eax
	movl	-20(%rbp), %esi
	subl	$1, %esi
	movslq	%esi, %rcx
	movq	-8(%rbp), %rdx
	movl	%eax, (%rdx,%rcx,4)
	movl	-24(%rbp), %eax
	movslq	-20(%rbp), %rcx
	movq	-8(%rbp), %rdx
	movl	%eax, (%rdx,%rcx,4)
LBB3_6:                                 ##   in Loop: Header=BB3_3 Depth=2
	jmp	LBB3_7
LBB3_7:                                 ##   in Loop: Header=BB3_3 Depth=2
	movl	-20(%rbp), %eax
	addl	$1, %eax
	movl	%eax, -20(%rbp)
	jmp	LBB3_3
LBB3_8:                                 ##   in Loop: Header=BB3_1 Depth=1
	jmp	LBB3_9
LBB3_9:                                 ##   in Loop: Header=BB3_1 Depth=1
	movl	-16(%rbp), %eax
	addl	$4294967295, %eax       ## imm = 0xFFFFFFFF
	movl	%eax, -16(%rbp)
	jmp	LBB3_1
LBB3_10:
	popq	%rbp
	ret
	.cfi_endproc

	.globl	_main
	.align	4, 0x90
_main:                                  ## @main
	.cfi_startproc
## BB#0:
	pushq	%rbp
Ltmp22:
	.cfi_def_cfa_offset 16
Ltmp23:
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
Ltmp24:
	.cfi_def_cfa_register %rbp
	subq	$144, %rsp
	movl	$8, %esi
	leaq	-48(%rbp), %rdi
	movq	___stack_chk_guard@GOTPCREL(%rip), %rax
	movq	(%rax), %rax
	movq	%rax, -8(%rbp)
	movl	$0, -12(%rbp)
	movq	L__ZZ4mainE1a(%rip), %rax
	movq	%rax, -48(%rbp)
	movq	L__ZZ4mainE1a+8(%rip), %rax
	movq	%rax, -40(%rbp)
	movq	L__ZZ4mainE1a+16(%rip), %rax
	movq	%rax, -32(%rbp)
	movq	L__ZZ4mainE1a+24(%rip), %rax
	movq	%rax, -24(%rbp)
	movq	L__ZZ4mainE1b(%rip), %rax
	movq	%rax, -80(%rbp)
	movq	L__ZZ4mainE1b+8(%rip), %rax
	movq	%rax, -72(%rbp)
	movq	L__ZZ4mainE1b+16(%rip), %rax
	movq	%rax, -64(%rbp)
	movq	L__ZZ4mainE1b+24(%rip), %rax
	movq	%rax, -56(%rbp)
	movq	L__ZZ4mainE1c(%rip), %rax
	movq	%rax, -112(%rbp)
	movq	L__ZZ4mainE1c+8(%rip), %rax
	movq	%rax, -104(%rbp)
	movq	L__ZZ4mainE1c+16(%rip), %rax
	movq	%rax, -96(%rbp)
	movq	L__ZZ4mainE1c+24(%rip), %rax
	movq	%rax, -88(%rbp)
	callq	__Z14selection_sortPii
	movl	$8, %esi
	leaq	-80(%rbp), %rdi
	callq	__Z11bubble_sortPii
	movl	$8, %esi
	leaq	-112(%rbp), %rdi
	callq	__Z14insertion_sortPii
	leaq	L_.str(%rip), %rdi
	movb	$0, %al
	callq	_printf
	movl	$0, -116(%rbp)
	movl	%eax, -120(%rbp)        ## 4-byte Spill
LBB4_1:                                 ## =>This Inner Loop Header: Depth=1
	cmpl	$8, -116(%rbp)
	jge	LBB4_4
## BB#2:                                ##   in Loop: Header=BB4_1 Depth=1
	leaq	L_.str1(%rip), %rdi
	movslq	-116(%rbp), %rax
	movl	-48(%rbp,%rax,4), %esi
	movb	$0, %al
	callq	_printf
	movl	%eax, -124(%rbp)        ## 4-byte Spill
## BB#3:                                ##   in Loop: Header=BB4_1 Depth=1
	movl	-116(%rbp), %eax
	addl	$1, %eax
	movl	%eax, -116(%rbp)
	jmp	LBB4_1
LBB4_4:
	leaq	L_.str2(%rip), %rdi
	movb	$0, %al
	callq	_printf
	movl	$0, -116(%rbp)
	movl	%eax, -128(%rbp)        ## 4-byte Spill
LBB4_5:                                 ## =>This Inner Loop Header: Depth=1
	cmpl	$8, -116(%rbp)
	jge	LBB4_8
## BB#6:                                ##   in Loop: Header=BB4_5 Depth=1
	leaq	L_.str1(%rip), %rdi
	movslq	-116(%rbp), %rax
	movl	-80(%rbp,%rax,4), %esi
	movb	$0, %al
	callq	_printf
	movl	%eax, -132(%rbp)        ## 4-byte Spill
## BB#7:                                ##   in Loop: Header=BB4_5 Depth=1
	movl	-116(%rbp), %eax
	addl	$1, %eax
	movl	%eax, -116(%rbp)
	jmp	LBB4_5
LBB4_8:
	leaq	L_.str3(%rip), %rdi
	movb	$0, %al
	callq	_printf
	movl	$0, -116(%rbp)
	movl	%eax, -136(%rbp)        ## 4-byte Spill
LBB4_9:                                 ## =>This Inner Loop Header: Depth=1
	cmpl	$8, -116(%rbp)
	jge	LBB4_12
## BB#10:                               ##   in Loop: Header=BB4_9 Depth=1
	leaq	L_.str1(%rip), %rdi
	movslq	-116(%rbp), %rax
	movl	-112(%rbp,%rax,4), %esi
	movb	$0, %al
	callq	_printf
	movl	%eax, -140(%rbp)        ## 4-byte Spill
## BB#11:                               ##   in Loop: Header=BB4_9 Depth=1
	movl	-116(%rbp), %eax
	addl	$1, %eax
	movl	%eax, -116(%rbp)
	jmp	LBB4_9
LBB4_12:
	movq	___stack_chk_guard@GOTPCREL(%rip), %rax
	movq	(%rax), %rax
	cmpq	-8(%rbp), %rax
	jne	LBB4_14
## BB#13:                               ## %SP_return
	movl	$0, %eax
	addq	$144, %rsp
	popq	%rbp
	ret
LBB4_14:                                ## %CallStackCheckFailBlk
	callq	___stack_chk_fail
	.cfi_endproc

	.section	__TEXT,__const
	.align	4                       ## @_ZZ4mainE1a
L__ZZ4mainE1a:
	.long	2                       ## 0x2
	.long	4                       ## 0x4
	.long	10                      ## 0xa
	.long	7                       ## 0x7
	.long	4                       ## 0x4
	.long	6                       ## 0x6
	.long	8                       ## 0x8
	.long	1                       ## 0x1

	.align	4                       ## @_ZZ4mainE1b
L__ZZ4mainE1b:
	.long	2                       ## 0x2
	.long	4                       ## 0x4
	.long	10                      ## 0xa
	.long	7                       ## 0x7
	.long	4                       ## 0x4
	.long	6                       ## 0x6
	.long	8                       ## 0x8
	.long	1                       ## 0x1

	.align	4                       ## @_ZZ4mainE1c
L__ZZ4mainE1c:
	.long	2                       ## 0x2
	.long	4                       ## 0x4
	.long	10                      ## 0xa
	.long	7                       ## 0x7
	.long	4                       ## 0x4
	.long	6                       ## 0x6
	.long	8                       ## 0x8
	.long	1                       ## 0x1

	.section	__TEXT,__cstring,cstring_literals
L_.str:                                 ## @.str
	.asciz	" Selection_Sort \n\n"

L_.str1:                                ## @.str1
	.asciz	"%d "

L_.str2:                                ## @.str2
	.asciz	" Bubble_Sort  \n\n"

L_.str3:                                ## @.str3
	.asciz	"Insertion_Sort \n\n"


.subsections_via_symbols
