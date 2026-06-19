document.addEventListener(
    "DOMContentLoaded",
    function(){

        const container =
            document.getElementById(
                "excel-table"
            );

        if(!container){
            return;
        }

        new Handsontable(
            container,
            {
                data: [
                    ["商品A",100],
                    ["商品B",200],
                    ["商品C",300],
                    ["", ""],
                    ["", ""],
                ],

                rowHeaders: true,

                colHeaders: [
                    "商品名",
                    "売上"
                ],

                licenseKey:
                    "non-commercial-and-evaluation"
            }
        );

    }
);