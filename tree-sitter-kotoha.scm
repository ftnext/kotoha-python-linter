; tree-sitter query tree-sitter-kotoha.scm examples/use_iterable.py
;
; examples/use_iterable.py
;   pattern: 0
;     capture: 0 - param_name, start: (5, 16), end: (5, 23), text: `numbers`
;     capture: 1 - type_name, start: (5, 25), end: (5, 29), text: `list`
;     capture: 2 - inner_type, start: (5, 30), end: (5, 33), text: `int`

(typed_parameter
  (identifier) @param_name
  type: (type
    (generic_type
      (identifier) @type_name
      (type_parameter
        (type
          (identifier) @inner_type))))
  (#eq? @type_name "list"))
