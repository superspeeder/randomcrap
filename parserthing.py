
test_data = """
*start [file:<file>]

*start [variables:<varible_declarations>&require:section(functions)]
<int> x = 10
<string> string_x = {convert:string(x)}
*end [variables]

*start [functions:<function_declarations:variants>&require:section(abstracts)]
#variant<convert@abstracts> string
return arguments.get_item(0).as_string()
*end [functions]

*start [abstracts:<function_declarations:abstracts>]
#function:abstract [convert&require:arguments(1)]
*end [abstracts]

*end [file]"""
