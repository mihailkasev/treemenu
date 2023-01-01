from django import template

from ..models import Thing

register = template.Library()


@register.inclusion_tag('menu/nested_menu.html', takes_context=True)
def draw_menu(context, menu):
    '''Строит древовидное меню.'''
    things = Thing.objects.filter(menu__title=menu)
    things_values = things.values()
    parent_things = [
        thing for thing in things_values.filter(
            parent=None).values()
    ]
    result_dict = {'things': parent_things}
    if context['request'].GET.get(menu) is not None:
        selected_thing_id = int(context['request'].GET[menu])
        selected_thing = things.get(id=selected_thing_id)
        selected_thing_id_list = get_selected_thing_id_list(
            selected_thing, parent_things, selected_thing_id
        )
        for thing in parent_things:
            if thing['id'] in selected_thing_id_list:
                thing['child_things'] = get_child_things(
                    things_values, thing['id'], selected_thing_id_list
                )
        result_dict = {'things': parent_things}
    result_dict['menu'] = menu
    result_dict['other_querystring'] = get_querystring(context, menu)

    return result_dict


def get_selected_thing_id_list(parent, parent_things, selected_thing_id):
    '''Получает "родителей" выбранного предмета.'''
    selected_thing_id_list = []

    while parent:
        selected_thing_id_list.append(parent.id)
        parent = parent.parent
    if not selected_thing_id_list:
        for thing in parent_things:
            if thing['id'] == selected_thing_id:
                selected_thing_id_list.append(selected_thing_id)
    return selected_thing_id_list


def get_child_things(things_values, current_thing_id, selected_thing_id_list):
    '''Получает вложенные предметы.'''
    thing_list = [
        thing for thing in things_values.filter(parent_id=current_thing_id)
    ]
    for thing in thing_list:
        if thing['id'] in selected_thing_id_list:
            thing['child_things'] = get_child_things(
                things_values, thing['id'],
                selected_thing_id_list
            )
    return thing_list


def get_querystring(context, menu):
    '''Получает новое меню.'''
    querystring_args = []
    for key in context['request'].GET:
        if key != menu:
            context_key = context['request'].GET[key]
            querystring_args.append(f'{key}={context_key}')
    querystring = ('&').join(querystring_args)
    return querystring
