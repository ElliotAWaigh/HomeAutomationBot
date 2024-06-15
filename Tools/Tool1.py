def context_for_Q1():
    required_context = {
        "context1": ["1", "2", "3"],
        "context2": ["1", "2", "3"]
    }
    optional_context = {
        "optional_context1": ["1", "2", "3"]
    }
    return required_context, optional_context

def action_for_Q1(context):
    if context['optional_context1'] == "default_value":
        context['years'] = "Default"
    return f"Actioning Information With Context Data from {context['context1'][0]} in {context['context2'][0]} {context['optional_context1']}"