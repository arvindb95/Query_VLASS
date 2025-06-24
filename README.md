# Query_VLASS
This is a code that uses astroquery to lookup VLASS quicklook images and download fits files of the relevant field. Code is adapted from [VLASS Quicklook Guide](https://science.nrao.edu/vlass/data-access/vlass-epoch-1-quick-look-users-guide). 

Here is an sample query : 
```bash

python query_vlass.py "16h33m29.41s" "−06d22m49.4s" 3

```

Sample output dialog :
```bash
The coordinates entered are present in more than one field!
0  :  https://ws.cadc-ccda.hia-iha.nrc-cnrc.gc.ca/caom2ops/sync?ID=nrao%3AVLASS%2FVLASS2.2.ql.T09t25.J163411-063000.10.2048.v1.I.iter1.image.pbcor.tt0.subim.fits&POS=CIRCLE+248.37254851836005+-6.380384681929677+0.05
1  :  https://ws.cadc-ccda.hia-iha.nrc-cnrc.gc.ca/caom2ops/sync?ID=nrao%3AVLASS%2FVLASS1.2.ql.T09t25.J163411-063000.10.2048.v1.I.iter1.image.pbcor.tt0.subim.fits&POS=CIRCLE+248.37254851836005+-6.380384681929677+0.05
2  :  https://ws.cadc-ccda.hia-iha.nrc-cnrc.gc.ca/caom2ops/sync?ID=nrao%3AVLASS%2FVLASS3.2.ql.T09t25.J163411-063000.10.2048.v1.I.iter1.image.pbcor.tt0.subim.fits&POS=CIRCLE+248.37254851836005+-6.380384681929677+0.05

Enter field you would like to download :

```

Enter the field id and the image will be downloaded in the same directory. 
