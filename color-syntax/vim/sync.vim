" SYNC syntax

if exists("b:current_syntax")
  finish
endif

" ---------- KEYWORDS ----------
syn keyword syncConditional IF ELSE ENDIF
syn keyword syncRepeat FOR ENDFOR
syn keyword syncKeyword FUNCTION END
syn keyword syncKeyword STRUCT ENDSTRUCT
syn keyword syncKeyword GLOBALS ENDGLOBALS
syn keyword syncKeyword RETURN

" ---------- TYPES ----------
syn keyword syncType INT FLOAT BOOL CHAR

" ---------- BUILTINS ----------
syn keyword syncBuiltin PRINT MALLOC_STRUCT FREE

" ---------- NUMBERS ----------
syn match syncNumber "\<\d\+\>"

" ---------- STRINGS ----------
syn region syncString start=+"+ end=+"+ keepend

" ---------- OPERATORS ----------
syn match syncOperator "->"
syn match syncOperator "[=+\-*/<>]"
syn keyword syncOperator AND OR NOT

" ---------- IDENTIFIERS ----------
" normal identifiers
syn match syncIdentifier "\<[a-zA-Z_][a-zA-Z0-9_]*\>"

" identifier before ->
syn match syncIdentifier "\<[a-zA-Z_][a-zA-Z0-9_]*\ze\s*->"

" struct field after ->
syn match syncField "\->\zs[a-zA-Z_][a-zA-Z0-9_]*"

" ---------- FUNCTION DECLARATIONS ----------
syn match syncFuncDecl "FUNCTION"
syn match syncFuncCall "\<\I\i*\>\s*"

" ---------- COMMENTS ----------
syntax match syncComment "//.*$" contains=NONE
syntax region syncComment start="/\*" end="\*/" keepend contains=NONE

" ---------- HIGHLIGHT LINKS (C-like) ----------
hi def link syncComment     Comment
hi def link syncConditional Conditional
hi def link syncRepeat      Repeat
hi def link syncKeyword     Keyword
hi def link syncType        Type
hi def link syncConstant    Constant
hi def link syncBuiltin     Function
hi def link syncFuncDecl    Function
hi def link syncFuncCall    Function
hi def link syncIdentifier  Identifier
hi def link syncField       Field
hi def link syncNumber      Number
hi def link syncString      String
hi def link syncOperator    Operator

let b:current_syntax = "sync"

