let price_formatter_setup = {
    minimumFractionDigits: 0,
    maximumFractionDigits: 2,
    style: 'currency',
    currency: 'USD',
};
const price_formatter_us = new Intl.NumberFormat('en-US', price_formatter_setup);

let price_formatter_setup_euro = {
    minimumFractionDigits: 0,
    maximumFractionDigits: 2,
    style: 'currency',
    currency: 'EUR',
};
const price_formatter_euro = new Intl.NumberFormat('en-US', price_formatter_setup_euro);

let num_formatter_setup = {
    minimumFractionDigits: 0,
    maximumFractionDigits: 2,
};
const num_formatter = new Intl.NumberFormat('en-US', num_formatter_setup);

let price_formatter_setup_low_values_us = {
    minimumFractionDigits: 0,
    maximumFractionDigits: 8,
    style: 'currency',
    currency: 'USD',
};
const price_formatter_low_values_us = new Intl.NumberFormat('en-US', price_formatter_setup_low_values_us);

let num_formatter_setup_low_values = {
    minimumFractionDigits: 0,
    maximumFractionDigits: 8,
};
const num_formatter_low_values = new Intl.NumberFormat('en-US', num_formatter_setup_low_values);

let price_formatter_setup_low_values_euro = {
    minimumFractionDigits: 0,
    maximumFractionDigits: 8,
    style: 'currency',
    currency: 'EUR',
};
const price_formatter_low_values_euro = new Intl.NumberFormat('en-US', price_formatter_setup_low_values_euro);
let price_volume_formatter_setup = {
    minimumFractionDigits: 0,
    maximumFractionDigits: 0,
    style: 'currency',
    currency: 'USD',
};
const price_volume_formatter = new Intl.NumberFormat('en-US', price_volume_formatter_setup);

function _get_formatter(val, is_usd_or_euro) {
    let p;
    if (val < 1) {
        if (is_usd_or_euro === "$") {
            p = price_formatter_low_values_us;
        } else if (is_usd_or_euro === "€") {
            p = price_formatter_low_values_euro;
        } else {
            p = num_formatter_low_values;
        }
    } else {
        if (is_usd_or_euro === "$") {
            p = price_formatter_us;
        } else if (is_usd_or_euro === "€") {
            p = price_formatter_euro;
        } else {
            p = num_formatter;
        }
    }
    return p
}
