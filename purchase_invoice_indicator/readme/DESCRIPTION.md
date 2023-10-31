This module introduces the is_invoice_issuer field to the Partner model
and the is_invoice field to the Invoice model. When an invoice is
created, the is_invoice_issuer value from the associated Partner or
Commercial Partner record is automatically propagated to the is_invoice
field in the new Invoice record.
