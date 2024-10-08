import numpy as np
import xarray as xr

from imap_processing.cdf.imap_cdf_manager import ImapCdfAttributes


def glows_l2(input_dataset: xr.Dataset, data_version: str) -> xr.Dataset:
    """
    Will process GLoWS L2 data from L1 data.
    Parameters
    ----------
    input_dataset
    data_version

    Returns
    -------

    """
    cdf_attrs = ImapCdfAttributes()
    cdf_attrs.add_instrument_global_attrs("glows")
    cdf_attrs.add_instrument_variable_attrs("glows", "l2")
    cdf_attrs.add_global_attribute("Data_version", data_version)



    # TODO: eliminate bad histograms per-epoch time based on l1b.flags using a mask with
    #  "active bad times" in ancillary file

    # TODO: compute averages for the range of L1B instances


    data_epoch = xr.DataArray(
        input_dataset["epoch"],
        name="epoch",
        dims=["epoch"],
        attrs=cdf_attrs.get_variable_attributes("epoch"),
    )

    logical_source = (
        input_dataset.attrs["Logical_source"][0]
        if isinstance(input_dataset.attrs["Logical_source"], list)
        else input_dataset.attrs["Logical_source"]
    )


    # TODO: the four spacecraft location/velocity values should probably each get
    # their own dimension/attributes
    eclipic_data = xr.DataArray(
        np.arange(3),
        name="ecliptic",
        dims=["ecliptic"],
        attrs=cdf_attrs.get_variable_attributes("ecliptic_dim"),
    )

    output_dataarrays = averaged_values(input_dataset)

    output_dataset = xr.Dataset(
        coords={
            "epoch": data_epoch,
            "ecliptic": eclipic_data,
            "bad_time_flags": bad_flag_data,
            "bins": bins, # not sure if this is needed
            "lightcurve": lightcurve # contains spin angle, photon_flux, exposure_times, flux_uncertainties, flags, ecliptic lon, ecliptic lat, and number of bins
        },
        attrs=cdf_attrs.get_global_attributes("imap_glows_l1b_hist"),
    )


def averaged_values(l1b_dataset: xr.Dataset):
    # most of the values from L1B are averaged over a day
    # For now, just average over the whole packet, but plan to make some kind of DB call in the future
    return NotImplementedError


def split_data_by_observational_day(input_dataset: xr.Dataset) -> xr.Dataset:
    """
    Return L1B data array for an observational day, given start and stop times.
    Parameters
    ----------
    input_dataset
        Input L1B dataset

    Returns
    -------
    list[xr.Dataset]
    """

    # Find the range of epoch values within the observational day.
    # This should be replaced with a query to the spin table to get the observational
    # days within the time range of the file and when those observational days
    # start and stop

    day_ends = [input_dataset["epoch"].data[0], input_dataset["epoch"].data[100], input_dataset["epoch"].data[-1]]
    print(day_ends)

    # TODO: this slice is inclusive on the start and end for some reason. When you
    #  replace this slice with the real spin data, figure that out.
    data_by_day = [input_dataset.sel(epoch=slice(day_ends[i], day_ends[i+1])) for i in range(len(day_ends)-1)]
    # print(data_by_day)

    print(data_by_day[0]['epoch'].data[0])
    print(data_by_day[0]['epoch'].data[-1])

    print(data_by_day[1]['epoch'].data[0])
    print(data_by_day[1]['epoch'].data[-1])


    # TODO: collect Histograml1B objects per observational day
    # For now, I guess just use a file to retrieve that info?

    # todo: run avg/std_dev methods on all the avg/std_dev variables
    # then put them and the histograms into the glows_l2 dataclass and run some method
    # to compute lightcurves.
    # then take that and put it into a dataset and return it out.
