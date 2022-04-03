class Color:
    default = 'default'
    gray = "gray"
    brown = "brown"
    orange = "orange"
    yellow = "yellow"
    green = "green"
    blue = "blue"
    purple = "purple"
    pink = "pink"
    red = "red"
    gray_background = "gray_background"
    brown_background = "brown_background"
    orange_background = "orange_background"
    yellow_background = "yellow_background"
    green_background = "green_background"
    blue_background = "blue_background"
    purple_background = "purple_background"
    pink_background = "pink_background"
    red_backgroun = "red_backgroun"


class FilterProperty:
    rich_text = 'rich_text'
    phone_number = 'phone_number'
    number = 'number'
    checkbox = 'checkbox'
    select = 'select'
    multi_select = 'multi-select'
    date = 'date'
    people = 'people'
    files = 'files'
    relation = 'relation'
    formula = 'formula'


class FilterCondition:
    class Text:
        # string
        equals = 'equals'
        does_not_equal = 'does_not_equal'
        contains = 'contains'
        does_not_contain = 'does_not_contain'
        starts_with = 'starts_with'
        ends_with = 'ends_with'
        # boolean (only True)
        is_empty = 'is_empty'
        is_not_empty = 'is_not_empty'

    class Number:
        # string
        equals = 'equals'
        does_not_equal = 'does_not_equal'
        greater_than = 'greater_than'
        less_than = 'less_than'
        greater_than_or_equal_to = 'greater_than_or_equal_to'
        less_than_or_equal_to = 'less_than_or_equal_to'
        # boolean (only True)
        is_empty = 'is_empty'
        is_not_empty = 'is_not_empty'

    class Checkbox:
        # boolean
        equals = 'equals'
        does_not_equal = 'does_not_equal'

    class Select:
        # string
        equals = 'equals'
        does_not_equal = 'does_not_equal'
        # boolean (only True)
        is_empty = 'is_empty'
        is_not_empty = 'is_not_empty'

    class MultiSelecte:
        # string
        contains = 'contains'
        does_not_contain = 'does_not_contain'
        # boolean (only True)
        is_empty = 'is_empty'
        is_not_empty = 'is_not_empty'

    # TODO Formula
    # TODO Rollup
    # TODO Relation
    # TODO Files
    # TODO People
    class Date:
        equals = 'equals'
        is_empty = 'is_empty'
        is_not_empty = 'is_not_empty'
        before = 'before'
        after = 'after'
        on_or_before = 'on_or_before'
        on_or_after = 'on_or_after'
        past_week = 'past_week'
        past_month = 'past_month'
        past_year = 'past_year'
        next_week = 'next_week'
        next_month = 'next_month'
        next_year = 'next_year'


class Language:
    abap = 'abap'
    arduino = 'arduino'
    bash = 'bash'
    basic = 'basic'
    c = 'c'
    clojure = 'clojure'
    coffeescript = 'coffeescript'
    cpp = 'c++'
    csharp = 'c#'
    css = 'css'
    dart = 'dart'
    diff = 'diff'
    docker = 'docker'
    elixir = 'elixir'
    elm = 'elm'
    erlang = 'erlang'
    flow = 'flow'
    fortran = 'fortran'
    fsharp = 'f#'
    gherkin = 'gherkin'
    glsl = 'glsl'
    go = 'go'
    graphql = 'graphql'
    groovy = 'groovy'
    haskell = 'haskell'
    html = 'html'
    java = 'java'
    javascript = 'javascript'
    json = 'json'
    julia = 'julia'
    kotlin = 'kotlin'
    latex = 'latex'
    less = 'less'
    lisp = 'lisp'
    livescript = 'livescript'
    lua = 'lua'
    makefile = 'makefile'
    markdown = 'markdown'
    markup = 'markup'
    matlab = 'matlab'
    mermaid = 'mermaid'
    nix = 'nix'
    objective_c = 'objective-c'
    ocaml = 'ocaml'
    pascal = 'pascal'
    perl = 'perl'
    php = 'php'
    plain_text = 'plain text'
    powershell = 'powershell'
    prolog = 'prolog'
    protobuf = 'protobuf'
    python = 'python'
    r = 'r'
    reason = 'reason'
    ruby = 'ruby'
    rust = 'rust'
    sass = 'sass'
    scala = 'scala'
    scheme = 'scheme'
    scss = 'scss'
    shell = 'shell'
    sql = 'sql'
    swift = 'swift'
    typescript = 'typescript'
    vb_net = 'vb.net'
    verilog = 'verilog'
    vhdl = 'vhdl'
    visual_basic = 'visual basic'
    webassembly = 'webassembly'
    xml = 'xml'
    yaml = 'yaml'
    jcps = 'java/c/c++/c#'
