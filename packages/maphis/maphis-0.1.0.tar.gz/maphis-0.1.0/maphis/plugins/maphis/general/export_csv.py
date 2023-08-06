import csv
import typing
from typing import Optional

from maphis.common.common import Info
from maphis.common.plugin import GeneralAction, ActionContext
from maphis.common.state import State
from maphis.plugins.maphis.general.common import _filter_by_NDArray, get_prop_tuple_list, \
    _group_measurements_by_sheet, _tabular_export_routine, _ndarray_export_routine, show_export_success_message


class ExportCSV(GeneralAction):
    """
    GROUP: export
    NAME: Export CSV
    KEY: export_csv
    DESCRIPTION: Export measurements to CSV.
    """
    def __init__(self, info: Optional[Info] = None):
        super().__init__(info)

    def __call__(self, state: State, context: ActionContext) -> None:
        prop_tuple_list = get_prop_tuple_list(context)
        nd_props, other_props = _filter_by_NDArray(prop_tuple_list, context)

        file_grouped_props = _group_measurements_by_sheet(other_props, context)

        file_names: typing.List[str] = []

        for group_name, prop_list in file_grouped_props.items():
            with open(context.storage.location / f'{context.current_label_name}_results_{group_name}.csv', 'w', newline='') as f:
                writer = csv.writer(f, dialect='excel')
                _tabular_export_routine(prop_list, writer.writerow, context)
            file_names.append(f'{context.current_label_name}_results_{group_name}.csv')

        sheet_nd_props = _group_measurements_by_sheet(nd_props, context)

        for group_name, prop_list in sheet_nd_props.items():
            with open(context.storage.location / f'{context.current_label_name}_results_{group_name}.csv', 'w', newline='') as f:
                writer = csv.writer(f, dialect='excel')
                _ndarray_export_routine(prop_list, writer.writerow, context)
            file_names.append(f'{context.current_label_name}_results_{group_name}.csv')

        # filenames = '\n'.join(file_names)
        # filenames = filenames[:-2]
        show_export_success_message(context.storage.location, file_names, context)
