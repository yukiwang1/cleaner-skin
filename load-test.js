import { group, sleep } from 'k6';
import http from 'k6/http';

// Version: 1.2
// Creator: WebInspector

export let options = {
	maxRedirects: 0,
	stages: [
		{ target: 100, duration: "30s" },
		{ target: 100, duration: "30s" }
	]
};

export default function () {

	group("page_1 - https://www.cleanerskin.io/product/41", function () {
		let req, res;
		req = [{
			"method": "get",
			"url": "https://www.cleanerskin.io/product/41",
			"params": {
				"cookies": {
					"session": ".eJwljktqBDEMBe_idRb6WVbPZRrZkkgIJNA9swq5ewxZvkdR1E8768r7vT2e1yvf2vkR7dE0qgbxYkYahtOXF0i3CvClGT2GzipbZO46DjvoOLxHTu8TxGpjTkw20DS0SIzR0wEoOhR3L4fQJRncAdEQK8k2pFOmcNshrzuv_xrcc91Xnc_vz_zax8QdMnSkcx8sS5BZZIIJGUJuL3YdS9rvHzM_Ppc.YdXu9Q.07won25G1wRK4K3aR7-1OJZMlw8"
				},
				"headers": {
					"Host": "www.cleanerskin.io",
					"Connection": "keep-alive",
					"Cache-Control": "max-age=0",
					"sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\", \"Google Chrome\";v=\"96\"",
					"sec-ch-ua-mobile": "?0",
					"sec-ch-ua-platform": "\"macOS\"",
					"Upgrade-Insecure-Requests": "1",
					"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
					"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
					"Sec-Fetch-Site": "same-origin",
					"Sec-Fetch-Mode": "navigate",
					"Sec-Fetch-User": "?1",
					"Sec-Fetch-Dest": "document",
					"Referer": "https://www.cleanerskin.io/search_results/mario",
					"Accept-Encoding": "gzip, deflate, br",
					"Accept-Language": "en-US,en;q=0.9"
				}
			}
		}, {
			"method": "get",
			"url": "https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css",
			"params": {
				"headers": {
					"sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\", \"Google Chrome\";v=\"96\"",
					"Referer": "https://www.cleanerskin.io/",
					"Origin": "https://www.cleanerskin.io",
					"sec-ch-ua-mobile": "?0",
					"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
					"sec-ch-ua-platform": "\"macOS\""
				}
			}
		}, {
			"method": "get",
			"url": "https://www.cleanerskin.io/static/search.png",
			"params": {
				"cookies": {
					"session": ".eJwljktqBDEMBe_idRb6WVbPZRrZkkgIJNA9swq5ewxZvkdR1E8768r7vT2e1yvf2vkR7dE0qgbxYkYahtOXF0i3CvClGT2GzipbZO46DjvoOLxHTu8TxGpjTkw20DS0SIzR0wEoOhR3L4fQJRncAdEQK8k2pFOmcNshrzuv_xrcc91Xnc_vz_zax8QdMnSkcx8sS5BZZIIJGUJuL3YdS9rvHzM_Ppc.YdXu9Q.07won25G1wRK4K3aR7-1OJZMlw8"
				},
				"headers": {
					"Host": "www.cleanerskin.io",
					"Connection": "keep-alive",
					"sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\", \"Google Chrome\";v=\"96\"",
					"If-Modified-Since": "Wed, 05 Jan 2022 18:00:49 GMT",
					"sec-ch-ua-mobile": "?0",
					"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
					"sec-ch-ua-platform": "\"macOS\"",
					"Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
					"Sec-Fetch-Site": "same-origin",
					"Sec-Fetch-Mode": "no-cors",
					"Sec-Fetch-Dest": "image",
					"Referer": "https://www.cleanerskin.io/product/41",
					"Accept-Encoding": "gzip, deflate, br",
					"Accept-Language": "en-US,en;q=0.9"
				}
			}
		}, {
			"method": "get",
			"url": "https://images.ulta.com/is/image/Ulta/2209926",
			"params": {
				"cookies": {
					"__ruid": "168695269-gn-8d-47-1p-bi2fsrqmqcrw8cpgpx2a-1637861563032",
					"__rcmp": "0!bj1zYjEsZj1zYixzPTAsYz0xODY5LHQ9MjAxODA5MjAuMjAwMA~~",
					"QuantumMetricUserID": "ad4d366f6ee9f90405d9e2afd058415c",
					"__rutma": "168695269-gn-8d-47-1p-bi2fsrqmqcrw8cpgpx2a-1637861563032.1639451100849.1639601147861.21.131.2"
				},
				"headers": {
					"sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\", \"Google Chrome\";v=\"96\"",
					"if-none-match": "\"ced3b8a19b535200500e69af7a6e6683\"",
					"if-modified-since": "Fri, 28 Jun 2019 13:35:52 GMT",
					"sec-ch-ua-mobile": "?0",
					"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
					"sec-ch-ua-platform": "\"macOS\"",
					"accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
					"sec-fetch-site": "cross-site",
					"sec-fetch-mode": "no-cors",
					"sec-fetch-dest": "image",
					"referer": "https://www.cleanerskin.io/",
					"accept-encoding": "gzip, deflate, br",
					"accept-language": "en-US,en;q=0.9"
				}
			}
		}, {
			"method": "get",
			"url": "https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js",
			"params": {
				"headers": {
					"sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\", \"Google Chrome\";v=\"96\"",
					"Referer": "https://www.cleanerskin.io/",
					"Origin": "https://www.cleanerskin.io",
					"sec-ch-ua-mobile": "?0",
					"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
					"sec-ch-ua-platform": "\"macOS\""
				}
			}
		}, {
			"method": "get",
			"url": "https://fonts.gstatic.com/s/outfit/v2/QGYvz_MVcBeNP4NJtEtqUYLknw.woff2",
			"params": {
				"headers": {
					"sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\", \"Google Chrome\";v=\"96\"",
					"Referer": "https://fonts.googleapis.com/",
					"Origin": "https://www.cleanerskin.io",
					"sec-ch-ua-mobile": "?0",
					"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
					"sec-ch-ua-platform": "\"macOS\""
				}
			}
		}, {
			"method": "get",
			"url": "https://www.cleanerskin.io/static/account_icon.png",
			"params": {
				"cookies": {
					"session": ".eJwljktqBDEMBe_idRb6WVbPZRrZkkgIJNA9swq5ewxZvkdR1E8768r7vT2e1yvf2vkR7dE0qgbxYkYahtOXF0i3CvClGT2GzipbZO46DjvoOLxHTu8TxGpjTkw20DS0SIzR0wEoOhR3L4fQJRncAdEQK8k2pFOmcNshrzuv_xrcc91Xnc_vz_zax8QdMnSkcx8sS5BZZIIJGUJuL3YdS9rvHzM_Ppc.YdXu9Q.07won25G1wRK4K3aR7-1OJZMlw8"
				},
				"headers": {
					"Host": "www.cleanerskin.io",
					"Connection": "keep-alive",
					"sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\", \"Google Chrome\";v=\"96\"",
					"sec-ch-ua-mobile": "?0",
					"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
					"sec-ch-ua-platform": "\"macOS\"",
					"Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
					"Sec-Fetch-Site": "same-origin",
					"Sec-Fetch-Mode": "no-cors",
					"Sec-Fetch-Dest": "image",
					"Referer": "https://www.cleanerskin.io/product/41",
					"Accept-Encoding": "gzip, deflate, br",
					"Accept-Language": "en-US,en;q=0.9",
					"If-Modified-Since": "Wed, 05 Jan 2022 18:00:49 GMT"
				}
			}
		}];
		res = http.batch(req);
		// Random sleep between 20s and 40s
		sleep(Math.floor(Math.random() * 20 + 20));
	});

}
