{% test is_integer(model, column_name) %}
select *
from {{ model }}
where try_cast({{ column_name }} as int) is null
  and {{ column_name }} is not null
{% endtest %}
