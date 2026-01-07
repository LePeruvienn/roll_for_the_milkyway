" Vim syntax file
" Language: SYNC

if exists("b:current_syntax")
  finish
endif

" ---------- KEYWORDS & CONTROL ----------
syn keyword syncConditional IF ELSE ENDIF ELIF
syn keyword syncRepeat      FOR ENDFOR WHILE ENDWHILE
syn keyword syncStatement   RETURN CONTINUE BREAK

" ---------- STRUCTURES & STORAGE ----------
syn keyword syncStructure   STRUCT ENDSTRUCT
syn keyword syncStorageClass GLOBALS ENDGLOBALS
syn keyword syncKeyword     FUNCTION END

" ---------- TYPES ----------
syn keyword syncType        INT FLOAT BOOL CHAR

" ---------- CONSTANTS ----------
syn keyword syncBoolean     TRUE FALSE
syn keyword syncConstant    NULL

" ---------- BUILTINS ----------
syn keyword syncBuiltin     PRINT PRINTERR MALLOC MALLOC_STRUCT FREE READ

" ---------- NUMBERS ----------
syn match syncNumber "\%([a-zA-Z_]\)\@<!-\?\d\+\(\.\d\+\)\?\%([a-zA-Z_]\)\@!"

" ---------- STRINGS ----------
syn region syncString start=+"+ end=+"+ keepend

" ---------- OPERATORS ----------
syn match   syncOperator "[=!+\-*/<>%&|^~,;]"
syn match   syncOperator "=="
syn match   syncOperator "<="
syn match   syncOperator ">="
syn match   syncOperator "\["
syn match   syncOperator "]"
syn match   syncOperator "->"
syn keyword syncOperator AND OR NOT

" ---------- IDENTIFIERS ----------
syn match syncIdentifier "\<[a-zA-Z_][a-zA-Z0-9_]*\>"
syn match syncIdentifier "\<[a-zA-Z_][a-zA-Z0-9_]*\ze\s*->"

" ---------- FUNCTIONS ----------
syn match syncFuncDecl "\<FUNCTION\>\s\+\%(\w\+\s\+\)\?\zs[a-zA-Z_][a-zA-Z0-9_]*"
syn match syncFuncCall "[a-zA-Z_][a-zA-Z0-9_]*\ze\s*("

" ---------- COMMENTS ----------
syn match  syncComment "//.*$" contains=syncTodo
syn region syncComment start="/\*" end="\*/" keepend contains=syncTodo
syn keyword syncTodo    TODO FIXME XXX NOTE contained

" ---------- HIGHLIGHT LINKS ----------
hi def link syncComment      Comment
hi def link syncTodo         Todo
hi def link syncConditional  Conditional
hi def link syncRepeat       Repeat
hi def link syncStatement    Statement
hi def link syncKeyword      Keyword
hi def link syncStructure    Structure
hi def link syncStorageClass StorageClass
hi def link syncType         Type
hi def link syncConstant     Constant
hi def link syncBoolean      Boolean
hi def link syncNumber       Number
hi def link syncString       String
hi def link syncOperator     Operator
hi def link syncBuiltin      Special
hi def link syncStructName Type
hi def link syncFuncDecl     Function
hi def link syncFuncCall     Function
hi def link syncIdentifier   Identifier

let b:current_syntax = "sync"

