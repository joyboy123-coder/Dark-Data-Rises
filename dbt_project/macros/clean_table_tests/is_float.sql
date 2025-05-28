{% test is_float(model, column_name) %}
select *
from {{ model }}
where try_cast({{ column_name }} as float) is null
  and {{ column_name }} is not null
{% endtest %}
