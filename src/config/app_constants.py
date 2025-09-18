from enum import Enum


class TundukApi(str, Enum):
    GetRealizationInvoice="/api/query/invoice/realization/all-documents"