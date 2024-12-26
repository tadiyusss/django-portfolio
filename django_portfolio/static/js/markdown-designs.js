function applyTailwind(container_id, dark_mode = false) {
    const container = `#${container_id}`;
    const darkClass = dark_mode ? 'dark' : '';

    $(`${container} h1`).addClass(`my-4 text-5xl font-semibold ${darkClass ? 'text-white' : ''}`);
    $(`${container} h2`).addClass(`my-4 text-4xl font-semibold ${darkClass ? 'text-white' : ''}`);
    $(`${container} h3`).addClass(`my-4 text-3xl font-semibold ${darkClass ? 'text-white' : ''}`);
    $(`${container} h4`).addClass(`my-4 text-2xl font-semibold ${darkClass ? 'text-white' : ''}`);
    $(`${container} h5`).addClass(`my-4 text-xl font-semibold ${darkClass ? 'text-white' : ''}`);
    $(`${container} h6`).addClass(`my-4 text-lg font-semibold ${darkClass ? 'text-white' : ''}`);
    $(`${container} p`).addClass(`w-full border border-gray-800 bg-gray-700 p-4`);
    $(`${container} p`).addClass(`my-2`);
    $(`${container} a`).addClass(`text-blue-500 ${darkClass ? 'text-blue-300' : ''}`);
    $(`${container} blockquote`).addClass(`border-l-4 ${darkClass ? 'border-gray-600' : 'border-gray-300'} pl-2`);
    $(`${container} ul`).addClass(`py-2 list-disc list-inside`);
    $(`${container} ol`).addClass(`py-2 list-decimal list-inside`);
    $(`${container} code`).addClass(`p-1 rounded ${darkClass ? 'bg-gray-700 text-gray-300' : ''}`);
    $(`${container} hr`).addClass(`my-8 ${darkClass ? 'border-gray-600' : ''}`);
    $(`${container} table`).addClass(`w-full my-2 ${darkClass ? 'bg-gray-800' : ''}`);
    $(`${container} thead`).addClass(`bg-gray-50 rounded-lg ${darkClass ? '' : 'border'} font-normal ${darkClass ? 'bg-gray-700 text-gray-300' : ''}`);
    $(`${container} th`).addClass(`font-semibold p-2 ${darkClass ? 'text-gray-300' : ''}`);
    $(`${container} tr`).addClass(`hover:bg-gray-50 ease duration-200 ${darkClass ? 'hover:bg-gray-700' : ''}`);
    $(`${container} td`).addClass(`p-2 border-b border-x ${darkClass ? 'border-gray-600' : ''}`);
    $(`${container} img`).addClass(`w-full rounded my-4`);
}