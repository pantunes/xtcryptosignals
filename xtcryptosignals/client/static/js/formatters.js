let price_formatter_setup = {
    minimumFractionDigits: 0,
    maximumFractionDigits: 2,
    style: 'currency',
    currency: 'USD',
};
const price_formatter = new Intl.NumberFormat('en-US', price_formatter_setup);

let num_formatter_setup = {
    minimumFractionDigits: 0,
    maximumFractionDigits: 2,
};
const num_formatter = new Intl.NumberFormat('en-US', num_formatter_setup);

let price_formatter_setup_low_values = {
    minimumFractionDigits: 0,
    maximumFractionDigits: 8,
    style: 'currency',
    currency: 'USD',
};
const price_formatter_low_values = new Intl.NumberFormat('en-US', price_formatter_setup_low_values);

let num_formatter_setup_low_values = {
    minimumFractionDigits: 0,
    maximumFractionDigits: 8,
};
const num_formatter_low_values = new Intl.NumberFormat('en-US', num_formatter_setup_low_values);

function _get_formatter(val, is_usd) {
    let p;
    if (val < 1) {
        if (is_usd) {
            p = price_formatter_low_values;
        } else {
            p = num_formatter_low_values;
        }
    } else {
        if (is_usd) {
            p = price_formatter;
        } else {
            p = num_formatter;
        }
    }
    return p
}
